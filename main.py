from scrapeVideos_class import scrapeVideos

if __name__ == '__main__':
    print("Started")
    pages = tuple(open("pages.txt", 'r'))

    for page in pages:
        page = page[:-1]
        print(page)
        scrapeVideos(page, './reels')
