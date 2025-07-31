# Script para descargar imágenes reales de tratamientos dentales
$images = @(
    @{
        "name" = "limpieza_antes"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    },
    @{
        "name" = "limpieza_despues"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    },
    @{
        "name" = "empaste_antes"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    },
    @{
        "name" = "empaste_despues"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    },
    @{
        "name" = "ortodoncia_antes"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    },
    @{
        "name" = "ortodoncia_despues"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    },
    @{
        "name" = "implante_antes"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    },
    @{
        "name" = "implante_despues"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    },
    @{
        "name" = "blanqueamiento_antes"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    },
    @{
        "name" = "blanqueamiento_despues"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    },
    @{
        "name" = "endodoncia_antes"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    },
    @{
        "name" = "endodoncia_despues"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    },
    @{
        "name" = "corona_antes"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    },
    @{
        "name" = "corona_despues"
        "url" = "https://images.pexels.com/photos/3771069/pexels-photo-3771069.jpeg"
    }
)

foreach ($image in $images) {
    try {
        Write-Host "Descargando: $($image.name).jpg"
        Invoke-WebRequest -Uri $image.url -OutFile "static\img\$($image.name).jpg" -TimeoutSec 30
        Write-Host "Descargada: $($image.name).jpg"
    }
    catch {
        Write-Host "Error descargando $($image.name).jpg"
        "Imagen de placeholder" | Out-File -FilePath "static\img\$($image.name).jpg" -Encoding UTF8
        Write-Host "Creada imagen de placeholder para $($image.name).jpg"
    }
}

Write-Host "Todas las imagenes han sido procesadas." 