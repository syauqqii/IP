from os import system, name

try:
    from requests import get
    from json import loads
    from argparse import ArgumentParser
except ModuleNotFoundError:
    try:
        import pip

        pip.main(["install", "requests"])
        pip.main(["install", "simplejson"])
        pip.main(["install", "argparse"])
        from requests import get
        from json import loads
    except ImportError:
        print("\n [!] Gagal import module.")
        exit(1)

TITLE = "WHO THE F ARE U?"
ENDPOINT_REQUEST_URL = "http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,proxy,query"


def clearScreen():
    system("cls" if name == "nt" else "clear")


def main(IP_INFO):
    clearScreen()
    URL_UPDATE = ENDPOINT_REQUEST_URL.format(IP_INFO)

    print(f"\n [#] {TITLE}")

    try:
        request = get(URL_UPDATE)

        if request.status_code == 200:
            respons = loads(request.text)

            if respons["status"] != "fail":
                print(f"\n  > IP          : {respons['query']}")
                print(f"  > ISP         : {respons['isp']}")
                print(f"  > Country     : {respons['country']}")
                print(f"  > Region      : {respons['regionName']}")
                print(f"  > City        : {respons['city']}")
                if respons["zip"] != "":
                    print(f"  > Zip-Code    : {respons['zip']}")
                print(f"  > Coordinate  : {respons['lat']}, {respons['lon']}")
                print(f"  > Time-Zone   : {respons['timezone']}")
                print(f"  > Org         : {respons['org']}")

                if respons["proxy"]:
                    print("\n [?] Kemungkinan menggunakan dns / proxy / vpn")
            else:
                print(f"\n [!] Terjadi kesalahan: {respons['message']}")
        else:
            print("\n [!] Gagal mengambil data IP. Kode status:", request.status_code)
    except Exception as e:
        print(f"\n [!] Terjadi kesalahan: {e}")


if __name__ == "__main__":
    try:
        parser = ArgumentParser(description=" - Who the F are u?")
        parser.add_argument(
            "-ip",
            "--ip",
            "-IP",
            "--IP",
            dest="IP_INFO",
            type=str,
            help="Give your F IP.",
        )

        args = parser.parse_args()
        if args.IP_INFO is None:
            print("\n [!] What the F are u doin?")
            exit(1)

        main(args.IP_INFO)
    except KeyboardInterrupt:
        exit(1)
