import requests, json

# API Document [ https://www.vultr.com/api/#api_name ]

"""
// API argument generator for register_methods (JavaScript for Chrome Console)
var h3s = document.getElementsByTagName("h3");
var result = [];
for(var i=0; i<h3s.length; i++) {
    var e = h3s[i], f = e.innerText.trim();
    if (!f.startsWith("/v1/")) continue;
    f = f.replace("/v1/", "");
    while(e != undefined)
    {
        if (e.innerText.indexOf("GET")>0)
        {
            result.push("            \"G " + f + "\"");
            break;
        }
        if (e.innerText.indexOf("POST")>0)
        {
            result.push("            \"P " + f + "\"");
            break;
        }
        e = e.nextElementSibling;
    }
}
console.log(result.join(",\n"));
"""


class API():
    def __init__(self, api_key=None):
        self.__headers = { "API-Key": api_key }
        self.__base_url = "https://api.vultr.com/v1/"
        self.register_methods([
            "G account/info",
            "G app/list",
            "G auth/info",
            "G backup/list",
            "P baremetal/app_change",
            "G baremetal/app_change_list",
            "G baremetal/bandwidth",
            "P baremetal/create",
            "P baremetal/destroy",
            "G baremetal/get_app_info",
            "G baremetal/get_user_data",
            "P baremetal/halt",
            "P baremetal/ipv6_enable",
            "P baremetal/label_set",
            "G baremetal/list",
            "G baremetal/list_ipv4",
            "G baremetal/list_ipv6",
            "P baremetal/os_change",
            "G baremetal/os_change_list",
            "P baremetal/reboot",
            "P baremetal/reinstall",
            "P baremetal/set_user_data",
            "P baremetal/tag_set",
            "P block/attach",
            "P block/create",
            "P block/delete",
            "P block/detach",
            "P block/label_set",
            "G block/list",
            "P block/resize",
            "P dns/create_domain",
            "P dns/create_record",
            "P dns/delete_domain",
            "P dns/delete_record",
            "P dns/dnssec_enable",
            "G dns/dnssec_info",
            "G dns/list",
            "G dns/records",
            "G dns/soa_info",
            "P dns/soa_update",
            "P dns/update_record",
            "P firewall/group_create",
            "P firewall/group_delete",
            "G firewall/group_list",
            "P firewall/group_set_description",
            "P firewall/rule_create",
            "P firewall/rule_delete",
            "G firewall/rule_list",
            "P iso/create_from_url",
            "P iso/destroy",
            "G iso/list",
            "G iso/list_public",
            "P network/create",
            "P network/destroy",
            "G network/list",
            "P objectstorage/create",
            "P objectstorage/destroy",
            "P objectstorage/label_set",
            "G objectstorage/list",
            "G objectstorage/list_cluster",
            "P objectstorage/s3key_regenerate",
            "G os/list",
            "G plans/list",
            "G plans/list_baremetal",
            "G plans/list_vc2",
            "G plans/list_vc2z",
            "G plans/list_vdc2",
            "G regions/availability",
            "G regions/availability_baremetal",
            "G regions/availability_vc2",
            "G regions/availability_vdc2",
            "G regions/list",
            "P reservedip/attach",
            "P reservedip/convert",
            "P reservedip/create",
            "P reservedip/destroy",
            "P reservedip/detach",
            "G reservedip/list",
            "P server/app_change",
            "G server/app_change_list",
            "P server/backup_disable",
            "P server/backup_enable",
            "P server/backup_get_schedule",
            "P server/backup_set_schedule",
            "G server/bandwidth",
            "P server/create",
            "P server/create_ipv4",
            "P server/destroy",
            "P server/destroy_ipv4",
            "P server/firewall_group_set",
            "G server/get_app_info",
            "G server/get_user_data",
            "P server/halt",
            "P server/ipv6_enable",
            "P server/iso_attach",
            "P server/iso_detach",
            "G server/iso_status",
            "P server/label_set",
            "G server/list",
            "G server/list_ipv4",
            "G server/list_ipv6",
            "G server/neighbors",
            "P server/os_change",
            "G server/os_change_list",
            "P server/private_network_disable",
            "P server/private_network_enable",
            "G server/private_networks",
            "P server/reboot",
            "P server/reinstall",
            "P server/restore_backup",
            "P server/restore_snapshot",
            "P server/reverse_default_ipv4",
            "P server/reverse_delete_ipv6",
            "G server/reverse_list_ipv6",
            "P server/reverse_set_ipv4",
            "P server/reverse_set_ipv6",
            "P server/set_user_data",
            "P server/start",
            "P server/tag_set",
            "P server/upgrade_plan",
            "G server/upgrade_plan_list",
            "P snapshot/create",
            "P snapshot/create_from_url",
            "P snapshot/destroy",
            "G snapshot/list",
            "P sshkey/create",
            "P sshkey/destroy",
            "G sshkey/list",
            "P sshkey/update",
            "P startupscript/create",
            "P startupscript/destroy",
            "G startupscript/list",
            "P startupscript/update",
            "P user/create",
            "P user/delete",
            "G user/list",
            "P user/update"
        ])

    def register_methods(self, endpoints):
        for ep in endpoints:
            setattr(self, ep[2:].replace("/", "_"),
                lambda path=ep[2:], fn=(ep[0]=="G") and self._get or self._post, **k:
                    fn(path, **k)
            )

    def _dictify(self, res):
        ok = (res.status_code == requests.codes.ok)
        if ok and res.text != "":
          j = json.loads(res.text, encoding = res.encoding)
        else:
          j = { "_error": not ok, "_status_code": res.status_code }
        return j

    def _get(self, path, **k):
        return self._dictify(requests.get(self.__base_url + path, headers=self.__headers, params=k))

    def _post(self, path, **k):
        return self._dictify(requests.post(self.__base_url + path, data=k, headers=self.__headers))


# some test cases
if __name__ == "__main__":
    api = API("YOUR_API_KEY")

    # public APIs
    print(json.dumps(api.os_list(), indent=2))
    print(json.dumps(api.regions_list(), indent=2))

    # needs valid API key
    print(json.dumps(api.server_list(), indent=2))
    print(json.dumps(api.plans_list(type="vc2"), indent=2))
    print(json.dumps(api.regions_availability(DCID=1), indent=2))

    # WARNING: this command changes your server's tag!
    print(json.dumps(api.server_tag_set(SUBID="YOUR_SUBSCRIPTION_ID", tag="tag-test"), indent=2))
