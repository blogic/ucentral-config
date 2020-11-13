{
	"ntp": {
		"enabled": 1,
		"enable_server": 1,
		"server": [
			"0.openwrt.pool.ntp.org",
			"1.openwrt.pool.ntp.org"
		]
	},
	"ssh": {
		"enable": 1,
		"Port": 22
	},
	"system": {
		"timezone": "CET-1CEST,M3.5.0,M10.5.0/3"
	},
	"log": {
		"log_proto": "udp",
		"log_ip": "192.168.11.23",
		"log_port": 12345,
		"log_hostname": "foo",
		"log_size": 128
	}
}
