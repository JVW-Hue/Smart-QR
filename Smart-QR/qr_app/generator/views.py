import qrcode
import io
import base64
from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import stripe
import json
from .models import QRCode

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    return render(request, 'generator/home.html')

def generate_qr(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content', '')
        color = data.get('color', '#000000')
        bg_color = data.get('background_color', '#ffffff')
        
        if not content:
            return JsonResponse({'error': 'Content is required'}, status=400)
        
        # Create QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(content)
        qr.make(fit=True)
        
        # Generate QR image
        qr_img = qr.make_image(fill_color=color, back_color=bg_color)
        
        # Add watermark for free version
        watermarked_img = add_watermark(qr_img)
        
        # Convert to base64
        buffer = io.BytesIO()
        watermarked_img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        # Save to database
        qr_code = QRCode.objects.create(
            content=content,
            color=color,
            background_color=bg_color
        )
        
        return JsonResponse({
            'success': True,
            'qr_id': str(qr_code.id),
            'image': f'data:image/png;base64,{img_str}'
        })
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def add_watermark(img):
    """Add watermark to QR code image"""
    # Convert to RGBA if not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Create watermark overlay
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Add text watermark
    try:
        font = ImageFont.truetype("arial.ttf", 12)
    except:
        font = ImageFont.load_default()
    
    text = "JVW"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Position at bottom right
    x = img.width - text_width - 10
    y = img.height - text_height - 10
    
    draw.text((x, y), text, fill=(128, 128, 128, 180), font=font)
    
    # Combine images
    watermarked = Image.alpha_composite(img, overlay)
    return watermarked.convert('RGB')

@csrf_exempt
def create_payment_intent(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        qr_id = data.get('qr_id')
        
        try:
            qr_code = get_object_or_404(QRCode, id=qr_id)
            
            # Create Stripe payment intent
            intent = stripe.PaymentIntent.create(
                amount=100,  # $1.00 in cents
                currency='usd',
                metadata={'qr_id': str(qr_id)}
            )
            
            qr_code.payment_intent_id = intent.id
            qr_code.save()
            
            return JsonResponse({
                'client_secret': intent.client_secret,
                'publishable_key': settings.STRIPE_PUBLISHABLE_KEY
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def confirm_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        payment_intent_id = data.get('payment_intent_id')
        
        try:
            # Verify payment with Stripe
            intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            
            if intent.status == 'succeeded':
                qr_id = intent.metadata.get('qr_id')
                qr_code = get_object_or_404(QRCode, id=qr_id)
                qr_code.is_paid = True
                qr_code.save()
                
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'error': 'Payment not completed'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def download_hd(request, qr_id):
    qr_code = get_object_or_404(QRCode, id=qr_id)
    
    if not qr_code.is_paid:
        return JsonResponse({'error': 'Payment required'}, status=403)
    
    # Generate HD QR code without watermark
    qr = qrcode.QRCode(version=1, box_size=20, border=5)
    qr.add_data(qr_code.content)
    qr.make(fit=True)
    
    qr_img = qr.make_image(
        fill_color=qr_code.color,
        back_color=qr_code.background_color
    )
    
    # Return as PNG download
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="qr_code_hd_{qr_id}.png"'
    qr_img.save(response, 'PNG')
    
    return response