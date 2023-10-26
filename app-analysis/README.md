## App analysis

This subdirectory contain the mobile data analysis code and app dataset

we use a Google Pixel 3a smart- phone running a licensed version of AppCensus runtime analysis technology. Specifically, we use a system-level instrumented variant of Android 9.0 (Pie), combined with Frida  scripts, that allows us to track runtime resource access by mobile apps (e.g., access to permission-protected Android APIs) and log all network traffic in plaintext (i.e., using MITM approaches to decrypt TLS traffic and other encodings). We use AppCensus visibility into app runtime behavior to detect potential instances of cross-device tracking and network fingerprinting, and to track how sensitive data is transmitted from IoT devices to companion apps, and then to remote servers. We pair the testing smartphone to each IoT device, then we use Android's Application Exerciser Monkey to generate synthetic user inputs for approximately five minutes. 

We believe and tested that this analysis can be reproduced with open-source tools like mitmproxy, frida and tcpdump.
