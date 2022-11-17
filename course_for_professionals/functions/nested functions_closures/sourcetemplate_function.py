def sourcetemplate(url):
    def make_url(**kwargs):
        return url + '?' * bool(kwargs) + '&'.join(sorted(f'{k}={v}' for k, v in kwargs.items()))
    return make_url


url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))