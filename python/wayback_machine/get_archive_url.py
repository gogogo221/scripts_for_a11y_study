from distutils import archive_util
from waybackpy import WaybackMachineCDXServerAPI
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"


def get_wayback_archive(url: str, year:int = 2022, month:int = 8, day:int = 15) -> list[str, str]:
    """
    gets 2 wayback machine archives of a page from 3 years and 6 years ago.
    """
    output_urls = []
    base_date = datetime(year, month, day)
    three_years_before_base = base_date - relativedelta(years=3)
    six_years_before_base = base_date - relativedelta(years=6)
    print(three_years_before_base.year)
    print(six_years_before_base)
    archive_target_dates = [three_years_before_base, six_years_before_base]
    for date in archive_target_dates:
        earliest = date - relativedelta(month=6)
        latest = date + relativedelta(month=6)
        cdx_api = WaybackMachineCDXServerAPI(url, USER_AGENT, start_timestamp=earliest.strftime("%Y%m"), end_timestamp=latest.strftime("%Y%m"))
        try:
            nearest_url = cdx_api.near(date.year, date.month)
            output_urls.append(nearest_url.archive_url)
        except:
            output_urls.append("NO URL")

    return output_urls
  
def main():
    urls = get_wayback_archive("evanevanstours.com", 2022, 5)
    print(urls)

if __name__ == "__main__":
    main()