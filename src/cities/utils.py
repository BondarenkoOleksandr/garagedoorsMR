import random

from cities.models import City, SEOCity

def city_seo():
    for city in City.objects.all():
        seo_title = city.name + 'Garage Door Repair, Installation & Maintenance Services'
        seo_description = f'Garage Doors Repair™ is a full-service garage door company in {city.name} that provides 24/7 residential & commercial repair, installation, and maintenance services!'
        seo_canonical = 'https://google.com.ua'
        seo_robots = 'INDEX, FOLLOW'
        seo_schema = """{
          "@context" : "http://schema.org",
          "@type": "LocalBusiness",
    
          "name" : "Garage Doors Repair",
    
          "logo" : "https://garagedoors.fun/static/img/logo.png",
    
          "url": "{Current url}",
    
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "Unit 1, Riverside Industrial Park, 16 Lyon Road",
            "addressRegion": "{city.name}",
            "postalCode": \"""" + str(random.randint(1, 500000)) + """\"
            },
          "telephone": "+10000000000",
    
          "openingHours": 
          [
            "Mo-Sa 00:00-23:59"
          ],
          "email" :"info@{domain}",
          "image" :\"""" + city.firstscreen.image.image.url + """ ",
          "vatID": "11965684",
    
          "description": "Garage Doors Repair™ is a full-service garage door company in {город} that provides 24/7 residential & commercial repair, installation, and maintenance services!"
          }
         }
        """
        seo_og = f"""<meta property="og:title" content="{city.firstscreen.title}">
        <meta property="og:site_name" content="Garage Doors Repair™">
        <meta property="og:url" content="current url">
        <meta property="og:description" content="Garage Doors Repair™ is a full-service garage door company in {city.name} that provides 24/7 residential & commercial repair, installation, and maintenance services!">
        <meta property="og:type" content="article">
        <meta property="og:image" content="{city.firstscreen.image.image.url}">"""

        SEOCity.objects.create(
            state=city,
            seo_title=seo_title,
            seo_description=seo_description,
            seo_canonical=seo_canonical,
            seo_robots=seo_robots,
            seo_schema=seo_schema,
            seo_og=seo_og,

        )

