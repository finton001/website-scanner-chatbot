import requests
from urllib.parse import urlparse

SECURITY_HEADERS = {
    'Strict-Transport-Security': 'HSTS ensures HTTPS connections are secure',
    'Content-Security-Policy': 'CSP prevents XSS and data injection attacks',
    'X-Content-Type-Options': 'Prevents MIME-type sniffing',
    'X-Frame-Options': 'Protects against clickjacking',
    'X-XSS-Protection': 'Legacy XSS protection (replaced by CSP)',
    'Referrer-Policy': 'Controls referrer information',
    'Permissions-Policy': 'Controls browser features',
    'Cache-Control': 'Controls caching behavior'
}

def scan_security_headers(target_url):
    result = {
        'target': target_url,
        'missing_headers': [],
        'present_headers': {},
        'summary': ''
    }
    
    try:
        response = requests.get(target_url, timeout=10, verify=False)
        headers = response.headers
        
        for header, description in SECURITY_HEADERS.items():
            header_value = headers.get(header)
            if header_value:
                result['present_headers'][header] = {
                    'value': header_value,
                    'description': description
                }
            else:
                result['missing_headers'].append({
                    'header': header,
                    'description': description
                })
        
        result['summary'] = f"Found {len(result['present_headers'])}/8 security headers. Missing {len(result['missing_headers'])} headers."
        
    except requests.exceptions.RequestException as e:
        result['error'] = str(e)
        result['summary'] = 'Scan failed'
    
    return result

if __name__ == '__main__':
    result = scan_security_headers('https://example.com')
    print(result)