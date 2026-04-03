# Get IPv4 address
$ip = Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.InterfaceAlias -notlike "*Loopback*" } | Select-Object -ExpandProperty IPAddress -First 1

# Get MAC address
$mac = Get-NetAdapter | Where-Object { $_.Status -eq "Up" } | Select-Object -ExpandProperty MacAddress -First 1

Write-Host "---------------------------"
Write-Host " Network Information Finder"
Write-Host "---------------------------"
Write-Host " Current IP Address:  $ip"
Write-Host " Current MAC Address: $mac"
Write-Host "---------------------------"
Pause
