import requests

def scrapper(url:str):
    response = requests.get(url).content
    print(response)

if __name__ == '__main__':
    url="https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3999934878&eBP=CwEAAAGRSPjOKBS-0yVm09ouiiRHx6IYi-Ey9CqM2QWEP8sN4eRKdVDNXKle2nbPuJw9gxB_ZgaQN0s3a9j8uxMyA4Pcz0WLETkv4pb287k9QhcFIIrVnyC3XjWb2NXMHjKR6NMyCmd2D5hlLLNWrRQY3Q9uVRBJkP2hhI5UnODzCcoK9XVpRlE0XQ29tcutYGGnRKgzfYopj2bHiSIVV8cPPgxZ5GKKYms6_mmCXMMp04AxscFI3mZFmO5I3APWf0xKOlY4_joQdwEMl9UyhOkkfzQpmVXSjJ_zLCrkR6wZgFh47daO0n7iy7n1JD6KK4PbxBivmLkG5pkdVGeebd6A6yVrZppjOgfZO7BT6LGiizLTDPpK9HVkhqaqaAGqoh6_J-UiY6qSe9GoOPUCnIefSVcv1NSTapN7Mon1sMQdHJIO42Wg7BoJ0FgQQKY3sXgr4kM&refId=feLp4yLFVrgwGF9%2FEmK%2FeQ%3D%3D&trackingId=1h"
    scrapper(url)