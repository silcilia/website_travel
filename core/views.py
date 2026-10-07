from urllib.parse import quote

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render

from .models import BookingInquiry


PACKAGES = [
    {'name': 'Palembang – Pahawang', 'location': 'Sumatera Selatan & Lampung', 'tag': 'Favorit', 'image': 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1000&q=80'},
    {'name': 'Palembang – Wayang Pahawang', 'location': 'Lampung', 'tag': 'Island Escape', 'image': 'https://images.unsplash.com/photo-1540202404-a2f29016b523?auto=format&fit=crop&w=1000&q=80'},
    {'name': 'Bangka', 'location': 'Kepulauan Bangka Belitung', 'tag': 'Beach', 'image': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80'},
    {'name': 'Bali – Lombok', 'location': 'Bali & Nusa Tenggara', 'tag': 'Best Seller', 'image': 'https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=1000&q=80'},
    {'name': 'Bandung', 'location': 'Jawa Barat', 'tag': 'City Escape', 'image': 'https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=1000&q=80'},
    {'name': 'Bromo', 'location': 'Jawa Timur', 'tag': 'Adventure', 'image': 'https://images.unsplash.com/photo-1516690561799-46d8f74f9abf?auto=format&fit=crop&w=1000&q=80'},
    {'name': 'Yogyakarta', 'location': 'Daerah Istimewa Yogyakarta', 'tag': 'Culture', 'image': 'https://images.unsplash.com/photo-1596402184320-417e7178b2cd?auto=format&fit=crop&w=1000&q=80'},
    {'name': 'Malaysia', 'location': 'Kuala Lumpur & sekitarnya', 'tag': 'International', 'image': 'https://images.unsplash.com/photo-1596422846543-75c6fc197f07?auto=format&fit=crop&w=1000&q=80'},
    {'name': 'Singapore', 'location': 'Singapore', 'tag': 'International', 'image': 'https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=1000&q=80'},
    {'name': 'Thailand – Bangkok', 'location': 'Bangkok, Thailand', 'tag': 'International', 'image': 'https://images.unsplash.com/photo-1508009603885-50cf7c579365?auto=format&fit=crop&w=1000&q=80'},
]

SERVICES = [
    ('Paket Wisata Domestik', 'Rute wisata Indonesia dengan itinerary yang praktis dan nyaman.'),
    ('Open Trip', 'Gabung perjalanan seru dengan jadwal dan itinerary yang sudah disiapkan.'),
    ('Private Tour', 'Liburan lebih fleksibel bersama keluarga, teman, atau pasangan.'),
    ('Family & Company Gathering', 'Perjalanan untuk bonding, gathering, dan kegiatan perusahaan.'),
    ('Study Tour', 'Kunjungan edukatif dengan perjalanan yang aman dan terorganisir.'),
    ('Outbound', 'Kegiatan team building dan outbound yang seru dan terarah.'),
    ('Custom Trip', 'Itinerary dibuat sesuai kebutuhan, waktu, dan budget perjalanan.'),
    ('Transportasi Wisata', 'Bus, kendaraan wisata, dan transportasi perjalanan sesuai kebutuhan.'),
]

GALLERY = [
    ('Momen perjalanan', 'https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?auto=format&fit=crop&w=1200&q=80'),
    ('Liburan pantai', 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80'),
    ('Explore Asia', 'https://images.unsplash.com/photo-1528181304800-259b08848526?auto=format&fit=crop&w=1200&q=80'),
    ('Sunrise adventure', 'https://images.unsplash.com/photo-1516690561799-46d8f74f9abf?auto=format&fit=crop&w=1200&q=80'),
    ('City escape', 'https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=1200&q=80'),
    ('Island getaway', 'https://images.unsplash.com/photo-1540202404-a2f29016b523?auto=format&fit=crop&w=1200&q=80'),
]


def home(request):
    whatsapp_number = settings.WHATSAPP_NUMBER
    whatsapp_text = quote('Halo Zhain Tour and Travel, saya ingin bertanya mengenai paket wisata.')
    return render(request, 'core/home.html', {
        'packages': PACKAGES,
        'services': SERVICES,
        'gallery': GALLERY,
        'whatsapp_url': f'https://wa.me/{whatsapp_number}?text={whatsapp_text}',
    })


def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        package = request.POST.get('package', '').strip()
        message = request.POST.get('message', '').strip()

        if not name or not phone:
            messages.error(request, 'Nama dan nomor WhatsApp wajib diisi.')
            return redirect('/#booking')

        BookingInquiry.objects.create(
            name=name,
            phone=phone,
            package=package,
            message=message,
        )
        whatsapp_text = quote(
            f'Halo Zhain Tour and Travel, saya {name}. Saya tertarik dengan paket {package or "wisata"}. '
            f'Nomor WhatsApp saya {phone}. {message}'
        )
        return redirect(f'https://wa.me/{settings.WHATSAPP_NUMBER}?text={whatsapp_text}')

    return redirect('/#booking')
