# Define the function to create JSON
function New-Json($basePath, $version) {
    $template = Get-Content -Path "$basePath.json.template"
    $template.Replace('$VERSION', $version) | Set-Content -Path "bucket/jgrpp/openttd-jgrpp-$version.json"
}

# Load the JSON data
$data = Get-Content -Path 'scripts/jgrpp_versions.json' | ConvertFrom-Json

# Loop through the versions
foreach ($version in $data.jgrpp_versions) {
    if ($data.noarm64 -contains $version) {
        Create-Json 'bucket/jgrpp/openttd-jgrpp-noarm64' $version
    } elseif ($data.diffname -contains $version) {
        Create-Json 'bucket/jgrpp/openttd-jgrpp-diffname' $version
    } elseif ($data.nobuild -contains $version) {
        continue
    } else {
        Create-Json 'bucket/jgrpp/openttd-jgrpp' $version
    }
}
