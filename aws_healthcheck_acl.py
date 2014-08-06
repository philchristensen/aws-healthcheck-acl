def fetch_newest_ranges():
    pass

def fetch_oldest_ranges():
    pass

def main():
    newest = fetch_newest_ranges()
    current = fetch_current_ranges()
    
    new = set(newest).difference(current)
    old = set(current).difference(newest)
    
    for ip_range in old:
        remove_range(ip_range)
    
    for ip_range in new:
        add_range(ip_range)

if(__name__ == '__main__'):
    main()