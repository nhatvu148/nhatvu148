$PSVersionTable
Write-Host "Congratulations! Your first script executed successfully"
# Start-Process PowerShell -WindowStyle Maximized -ArgumentList 'Get-Date; Read-Host "Press Enter"'
# echo "Hello!" && echo "World!"
# Start-Process -FilePath "powershell" -Verb RunAs
# $argList = "-NoExit -NoProfile Write-Host 'hello world'"
# Start-Process ping -ArgumentList 'google.com' -RedirectStandardOutput output.txt -RedirectStandardError err.txt
# Get-Content -Path output.txt

# $argList = "-NoExit -NoProfile cmd.exe @cmd /k 'cd ./client && yarn && yarn start'"
# Start-Process -FilePath powershell -WorkingDirectory ./ -ArgumentList $argList
# pwsh -c { $PSVersionTable.PSVersion }
# Start-Process pwsh '-c', 'echo "hello"; sleep 1; echo "two"; sleep 1; echo "goodbye"'

# for ($x = '' ; $x.length -le 30; $x = $x + 'x') {
#     Write-Host $x
#     Start-Sleep -Milliseconds 20
# }

# for ($num = 1 ; $num -le 10 ; $num++) { "I count $num" }

# $colors = @("Green", "Cyan", "Red", "Magenta", "Yellow", "White")
# for (($x = ''), ($fgcolor = $colors | Get-Random) ; $x.length -le 30; ($x = $x + 'x'), ($fgcolor = $colors | Get-Random)) {
#     Write-Host $x -ForegroundColor $fgcolor
#     Start-Sleep -Milliseconds 20
# }

# for ($counter = 1; $counter -le 100; $counter++ ) {
#     # ADD YOUR CODE HERE
#     Write-Progress -Activity "Update Progress" -Status "$counter% Complete:" -PercentComplete $counter;
# }

# for ($seconds = 10; $seconds -gt -1; $seconds--) {
#     Write-Host -NoNewLine ("`rseconds remaining: " + ("{0:d4}" -f $seconds))
#     Start-Sleep -Seconds 1
# }

# # Set the number of minutes to countdown from
# $minutes = 1
# for ($minutes--; $minutes -gt -1; $minutes--) {
#     for ($seconds = 59 ; $seconds -gt -1 ; $seconds--) {
#         $remaining = ("{0}:{1}" -f ("{0:d4}" -f $minutes), ("{0:d2}" -f $seconds))
#         Write-Host "`r$remaining" -NoNewline
#         Start-Sleep -Seconds 1
#     }
# }

# $num = Read-Host "Input a number"
# $isPrime = $true
# for ($y = 2 ; $y -lt $num ; $y++ ) {
#     if (($num / $y) -is [int]) {
#         Write-Host "$num is not a prime number"
#         $isPrime = $false
#         break
#     }
# }
# if ($isPrime -eq $true) {
#     Write-Host "$num is a prime number"
# }

$Object = [System.DateTime]::Now
$Object.AddHours(15)

# Get-PSDrive | ?{$_.Free -gt 1} | %{$Count = 0; Write-Host "";} { $_.Name + ": Used: " + "{0:N2}" -f ($_.Used/1gb) + " Free: " + "{0:N2}" -f ($_.free/1gb) + " Total: " + "{0:N2}" -f (($_.Used/1gb)+($_.Free/1gb)); $Count = $Count + $_.Free;}{Write-Host"";Write-Host "Total Free Space " ("{0:N2}" -f ($Count/1gb)) -backgroundcolor magenta}

# Get-PSDrive | Where-Object { $_.Free -gt 1 } 
# Get-PSDrive | Where-Object { $_.Free -gt 1 } | Select-Object Root, Used, Free
# Get-PSDrive | Where-Object { $_.Free -gt 1 } | Select-Object *
# Get-PSDrive | Where-Object { $_.Free -gt 1 } | ForEach-Object { "zebra" }
# Get-PSDrive | Where-Object { $_.Free -gt 1 } | ForEach-Object { Write-Host "Free space for" $_.Root "is" ($_.Free / 1gb) -ForegroundColor Red }
# Get-PSDrive | Where-Object { $_.Free -gt 1 } | ForEach-Object { Write-Host "Free space for" $_.Root "is" ("{0:N2}" -f ($_.Free / 1gb)) -ForegroundColor Red }
# Get-PSDrive | Where-Object { $_.Free -gt 1 } | ForEach-Object { $c = 0; Write-Host "This step only runs once" } { $c = $c + 1;  Write-Host "This command runs once for each object in the pipe" $c } { Write-Host "This step runs once everything is done. The value of c is" $c }
# "{0:N0}" -f 1000000000000
# "{0:N2}" -f 1000000000000
# "{0:C2}" -f 1000000000000
# "{0:P2}" -f 1000000000000

Test-Path “c:\test.txt”  
Test-Path “c:\test2.txt” 
New-Item -ItemType File “c:\test.txt”  
If (!(Test-Path “c:\test.txt”)){ New-Item -ItemType File “c:\test.txt” } 
Test-Path -Path "HKLM:\Software\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell" 
Test-Path $pshome\pwsh.exe -NewerThan "July 24, 2019" 

Get-ExecutionPolicy 
Set-ExecutionPolicy -ExecutionPolicy 

$creds = Get-Credential 

Invoke-Command -ComputerName svr01 -Credential $creds -ScriptBlock { Get-ExecutionPolicy} 
Invoke-Command -ComputerName svr01 -Credential $creds -FilePath “e:\scripts\demo.ps1” 

Enter-PSSession -ComputerName svr01 -Credential $creds
Exit-PSSession 