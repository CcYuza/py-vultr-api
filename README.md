# py-vultr-api
Simple Python wrapper of Vultr API [ https://www.vultr.com/api ]

## Feature
- Supports all API calls
- Generated from Vultr's API reference

## Example
```python
import vultrapi

# initialize
api = vultrapi.API("YOUR_API_KEY")

# enumerate
print("Supported functions:")
for v in dir(api):
	if not v.startswith('_'): print('\t' + v)

# public APIs
print(json.dumps(api.os_list(), indent=2))
print(json.dumps(api.regions_list(), indent=2))
print(json.dumps(api.plans_list(type="vc2"), indent=2))
print(json.dumps(api.regions_availability(DCID=1), indent=2))

# private APIs, needs valid API key
print(json.dumps(api.user_list(), indent=2))
print(json.dumps(api.server_list(), indent=2))
print(json.dumps(api.server_tag_set(SUBID="YOUR_SUBSCRIPTION_ID", tag="tag-test"), indent=2))
```