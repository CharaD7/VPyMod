services = {
    'ftp': 21,
    'ssh': 22,
    'smtp': 25,
    'http': 80
}
banner = "FreeFloat FTP Server"

print(f"[+] Found vuln with FTP on port {services['ftp']}")
