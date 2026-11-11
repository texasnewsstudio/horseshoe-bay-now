HORSESHOE BAY NOW — LIVE DASHBOARD REVISION 5

Cloudflare Pages dashboard Direct Upload: Upload this ZIP to the existing project as a PRODUCTION deployment.
No Pages Functions, no server-side code, no API keys.

WHAT WORKS:
- NWS current hourly forecast, wind, humidity, alerts, daily and golf weather.
- Texas city forecast temperatures (where NWS browser calls succeed).
- USGS Lake LBJ reservoir elevation: station 08152500, parameter 00062. Only displays readings newer than 48 hours; if CORS/feed unavailable, shows a clear error.
- TradingView market overview: embedded third-party data, may be delayed.
- OpenStreetMap/Overpass concierge local-place finder (not a true autonomous AI agent).
- Photo assets included locally, with natural proportions; no crop.

NOT YET CONNECTED:
- PayPal requires your actual PayPal payment URL.
- Lake water temperature: no verified live source.
- Real-time boat availability, golf tee times, and AI booking: require providers.
- LCRA reservoir data fallback: direct browser access may be blocked.

The panorama is a design image and includes printed words. It is not a live data panel.
To confirm you deployed the new version, look for 'Live dashboard revision 5' in the footer.

CONCIERGE UPDATE (REVISION 15 PATCH):
- Improved free on-page concierge: understands common natural-language requests and searches public OpenStreetMap business data.
- Added a backup map-search endpoint, additional categories, and map/call links.
- No API keys, accounts, or new fees. The existing photos, panels and layout are preserved.
- This is NOT yet a true AI conversational agent. Such an agent needs a securely configured AI backend, which is not included; never expose private API keys in index.html.
- Listings may be incomplete; no bookings or live availability are claimed.
