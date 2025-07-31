# Script para crear imágenes de prueba
$images = @(
    "limpieza_antes", "limpieza_despues",
    "empaste_antes", "empaste_despues", 
    "ortodoncia_antes", "ortodoncia_despues",
    "implante_antes", "implante_despues",
    "blanqueamiento_antes", "blanqueamiento_despues",
    "endodoncia_antes", "endodoncia_despues",
    "corona_antes", "corona_despues"
)

foreach ($image in $images) {
    $content = if ($image -like "*antes*") { "Antes" } else { "Después" }
    $content | Out-File -FilePath "static\img\$image.jpg" -Encoding UTF8
    Write-Host "Creada: $image.jpg"
}

Write-Host "Todas las imágenes han sido creadas." 