# bandcamp-feeds

`bandcamp-feeds` is a JSON Feed generator for [Bandcamp](https://bandcamp.com/) artist and label pages; it naïvely processes their HTML, so I expect it to break eventually.

## Usage

Because artist pages are hosted at *subdomains* of `bandcamp.com`, requests to `bandcamp-feeds` that don't specify an artist or label will yield a 500 Internal Server Error: requests to `https://.bandcamp.com` are invalid.

Instead, specify an artist or label page. For example: [`https://bandcamp-feeds-url.com/slift`](https://us-central1-arxiv-feeds.cloudfunctions.net/bandcamp-feeds/slift).

## Resources

+ `bandcamp-feeds` is built with [`jsonfeed-wrapper`](https://github.com/lukasschwab/jsonfeed-wrapper) and [`jsonfeed`](https://github.com/lukasschwab/jsonfeed).
+ [The feed is live here.](https://us-central1-arxiv-feeds.cloudfunctions.net/bandcamp-feeds) See [**Usage**](https://github.com/lukasschwab/bandcamp-feeds#usage) above.

An example of the raw HTML structure being processed into an item:

```html
<li class="music-grid-item square first-four" data-band-id="821915681" data-bind="css: {'featured': featured()}" data-item-id="album-467107251">
  <a href="/album/space-is-the-key">
    <div class="art">
      <img alt="" src="https://f4.bcbits.com/img/a3300867366_2.jpg"/>
    </div>
    <p class="title">Space Is The Key</p>
  </a>
</li>
```

## To do

+ Support feeds for tags.
