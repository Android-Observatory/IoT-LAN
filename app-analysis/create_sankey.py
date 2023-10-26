import plotly.graph_objects as go

flows = {
    'Amazon echo': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'SSDP': ['device name', 'model name', 'OS version', 'display name', 'UUIDs', 'Outdated OS'],
        'mDNS': ['MAC addr', 'device name', 'model name', 'display name'],
    },

    'Tuya Camera': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'TuyaLP': ['GWid Product key'],
    },


    'TP-Link plug/bulb': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'TPLink SHP': ['MAC addr', 'device name', 'model name', 'display name', 'OEM id', 'Geolocation']
    },
    
    'facebook portal': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'mDNS': ['MAC addr', 'device name', 'model name', 'display name'],
    },
    
    'Samsung Fridge': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'mDNS': ['MAC addr', 'device name', 'model name', 'display name'],
    },
    
    'Apple TV': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'mDNS': ['MAC addr', 'device name', 'model name', 'display name'],
    },
    
    'Aqara hub': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'mDNS': ['MAC addr', 'device name', 'model name', 'display name'],
    },

    'Google TV/Chromecast': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'mDNS': ['MAC addr', 'device name', 'model name', 'display name'],
    },

    'Dlink camera': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'mDNS': ['MAC addr', 'device name', 'model name', 'display name'],
    },

    'Homepod': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'mDNS': ['MAC addr', 'device name', 'model name', 'display name'],
    },

    'Roku TV': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'mDNS': ['MAC addr', 'device name', 'model name', 'display name'],
    },
    
    'Amazon fireTV': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'SSDP': ['device name', 'model name', 'OS version', 'display name', 'UUIDs', 'Outdated OS'],
        'mDNS': ['MAC addr', 'device name', 'model name', 'display name'],
    },
    
    'Google home/nest': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'SSDP': ['device name', 'model name', 'OS version', 'display name', 'UUIDs', 'Outdated OS'],
        'mDNS': ['MAC addr', 'device name', 'model name', 'display name'],
    },
    
    'LG tv': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'SSDP': ['device name', 'model name', 'OS version', 'display name', 'UUIDs', 'Outdated OS'],
    },
    
    'philips hub': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'SSDP': ['device name', 'model name', 'OS version', 'display name', 'UUIDs', 'Outdated OS'],
        'mDNS': ['MAC addr', 'device name', 'model name', 'display name'],
    },
    'wemo plug': {
        'ARP': ['MAC addr'],
        'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
        'SSDP': ['device name', 'model name', 'OS version', 'display name', 'UUIDs', 'Outdated OS'],
    },
    # 'Echodot3a': {
    #     'ARP': ['Mac'],
    #     'DHCP': ['MAC addr', 'device name', 'model name', 'OS version', 'display name', 'Outdated OS'],
    # }
}

# Define the flow values for each source
flow_values = {
    'Amazon echodot': 22,
    # 'facebook portal': 2,
    # 'Google home/nest': 5,
    # Add other devices here with their corresponding values if needed...
}

labels = list(flows.keys()) + list(set(k for i in flows.values() for k in i.keys())) + list(set(j for i in flows.values() for v in i.values() for j in v))

source = []
target = []
value = []

# Map each source to its intermediates and each intermediate to its targets
for src, intermediates in flows.items():
    for intermediate, tgts in intermediates.items():
        source.append(labels.index(src))
        target.append(labels.index(intermediate))
        value.append(flow_values.get(src, 1))  # Get the value from the flow_values dictionary. If it doesn't exist, use a default value of 1
        for tgt in tgts:
            source.append(labels.index(intermediate))
            target.append(labels.index(tgt))
            value.append(1)  # Assume an equal flow of 1 for the intermediates to targets

colors = ['red'] * len(flows.keys()) + ['blue'] * len(set(k for i in flows.values() for k in i.keys())) + ['green'] * len(set(j for i in flows.values() for v in i.values() for j in v))

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=.5),
        label=labels,
        color=colors
    ),
    link=dict(
        source=source,
        target=target,
        value=value
    )
)])

fig.update_layout(font_size=12, height=550, width=800)
fig.show()

