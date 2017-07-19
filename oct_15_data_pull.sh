#!/bin/sh

GREP_OPTIONS=''

cookiejar=$(mktemp cookies.XXXXXXXXXX)
netrc=$(mktemp netrc.XXXXXXXXXX)
chmod 0600 "$cookiejar" "$netrc"
function finish {
  rm -rf "$cookiejar" "$netrc"
}

trap finish EXIT
WGETRC="$wgetrc"

prompt_credentials() {
    echo "Enter your Earthdata Login or other provider supplied credentials"
    read -p "Username (hannah.n.93): " username
    username=${username:-hannah.n.93}
    read -s -p "Password: " password
    echo "\nmachine urs.earthdata.nasa.gov\tlogin $username\tpassword $password" >> $netrc
    echo
}

exit_with_error() {
    echo
    echo "Unable to Retrieve Data"
    echo
    echo $1
    echo
    echo "http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.31/MOD14.A2015304.1410.006.2015317095514.hdf"
    echo
    exit 1
}

prompt_credentials

  detect_app_approval() {
    approved=`curl -s -b "$cookiejar" -c "$cookiejar" -L --max-redirs 2 --netrc-file "$netrc" http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.31/MOD14.A2015304.1410.006.2015317095514.hdf -w %{http_code} | tail  -1`
    if [ "$approved" -ne "302" ]; then
        # User didn't approve the app. Direct users to approve the app in URS
        exit_with_error "Please ensure that you have authorized the remote application by visiting the link below "
    fi
}

setup_auth_curl() {
    # Firstly, check if it require URS authentication
    status=$(curl -s -z "$(date)" -w %{http_code} http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.31/MOD14.A2015304.1410.006.2015317095514.hdf | tail -1)
    if [[ "$status" -ne "200" && "$status" -ne "304" ]]; then
        # URS authentication is required. Now further check if the application/remote service is approved.
        detect_app_approval
    fi
}

setup_auth_wget() {
    # The safest way to auth via curl is netrc. Note: there's no checking or feedback
    # if login is unsuccessful
    touch ~/.netrc
    chmod 0600 ~/.netrc
    credentials=$(grep 'machine urs.earthdata.nasa.gov' ~/.netrc)
    if [ -z "$credentials" ]; then
        cat "$netrc" >> ~/.netrc
    fi
}

    fetch_urls() {
    if command -v curl >/dev/null 2>&1; then
        setup_auth_curl
        while read -r line; do
            curl -f -b "$cookiejar" -c "$cookiejar" -L --netrc-file "$netrc" -Og -- $line && echo || exit_with_error "Command failed with error. Please retrieve the data manually."
        done;
    elif command -v wget >/dev/null 2>&1; then
        # We can't use wget to poke provider server to get info whether or not URS was integrated without download at least one of the files.
        echo
        echo "WARNING: Can't find curl, use wget instead."
        echo "WARNING: Script may not correctly identify Earthdata Login integrations."
        echo
        setup_auth_wget
        while read -r line; do
        wget --load-cookies "$cookiejar" --save-cookies "$cookiejar" --keep-session-cookies -- $line && echo || exit_with_error "Command failed with error. Please retrieve the data manually."
        done;
    else
        exit_with_error "Error: Could not find a command-line downloader.  Please install curl or wget"
    fi
}

fetch_urls <<'EDSCEOF'
  http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.31/MOD14.A2015304.1410.006.2015317095514.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.31/MOD14.A2015304.0200.006.2015317095814.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.30/MOD14.A2015303.1325.006.2015317094358.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.30/MOD14.A2015303.0115.006.2015317095017.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.29/MOD14.A2015302.1425.006.2015317094002.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.29/MOD14.A2015302.1420.006.2015317094008.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.29/MOD14.A2015302.0210.006.2015317094258.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.29/MOD14.A2015302.0035.006.2015317094229.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.28/MOD14.A2015301.0130.006.2015317094030.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.27/MOD14.A2015300.1435.006.2015317092648.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.27/MOD14.A2015300.1255.006.2015317093014.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.27/MOD14.A2015300.0225.006.2015317092040.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.27/MOD14.A2015300.0045.006.2015317091939.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.26/MOD14.A2015299.1350.006.2015317092126.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.26/MOD14.A2015299.0140.006.2015317091934.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.25/MOD14.A2015298.1445.006.2015317091356.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.25/MOD14.A2015298.1310.006.2015317091635.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.25/MOD14.A2015298.1305.006.2015317091632.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.25/MOD14.A2015298.0100.006.2015317091415.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.25/MOD14.A2015298.0055.006.2015317091654.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.24/MOD14.A2015297.1405.006.2015317090911.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.24/MOD14.A2015297.1400.006.2015317090920.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.24/MOD14.A2015297.0155.006.2015317091000.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.24/MOD14.A2015297.0150.006.2015317091007.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.23/MOD14.A2015296.1320.006.2015306105431.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.23/MOD14.A2015296.0110.006.2015306105809.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.22/MOD14.A2015295.1415.006.2015306105526.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.22/MOD14.A2015295.0205.006.2015306105834.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.22/MOD14.A2015295.0030.006.2015306105836.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.22/MOD14.A2015295.0025.006.2015306105843.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.21/MOD14.A2015294.1335.006.2015306103303.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.21/MOD14.A2015294.1330.006.2015306103243.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.21/MOD14.A2015294.0125.006.2015306102352.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.21/MOD14.A2015294.0120.006.2015306102402.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.20/MOD14.A2015293.1430.006.2015306102708.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.20/MOD14.A2015293.1425.006.2015306102702.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.20/MOD14.A2015293.0220.006.2015306102447.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.20/MOD14.A2015293.0215.006.2015306102506.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.20/MOD14.A2015293.0040.006.2015306102424.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.19/MOD14.A2015292.1345.006.2015306095447.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.19/MOD14.A2015292.0135.006.2015306100303.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.18/MOD14.A2015291.1440.006.2015306094821.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.18/MOD14.A2015291.1305.006.2015306094822.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.18/MOD14.A2015291.1300.006.2015306094816.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.18/MOD14.A2015291.0055.006.2015306095557.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.18/MOD14.A2015291.0050.006.2015306095605.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.17/MOD14.A2015290.1400.006.2015306091602.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.17/MOD14.A2015290.1355.006.2015306091549.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.17/MOD14.A2015290.0150.006.2015306091145.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.17/MOD14.A2015290.0145.006.2015306091156.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.16/MOD14.A2015289.1450.006.2015306090303.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.16/MOD14.A2015289.1315.006.2015306090306.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.16/MOD14.A2015289.0105.006.2015306090840.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.15/MOD14.A2015288.1410.006.2015306104239.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.15/MOD14.A2015288.0200.006.2015306104602.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.14/MOD14.A2015287.1325.006.2015306104223.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.14/MOD14.A2015287.0115.006.2015306101047.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.13/MOD14.A2015286.1420.006.2015306100714.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.13/MOD14.A2015286.0210.006.2015306101207.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.13/MOD14.A2015286.0035.006.2015306100921.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.13/MOD14.A2015286.0030.006.2015306100901.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.12/MOD14.A2015285.1340.006.2015306100600.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.12/MOD14.A2015285.0130.006.2015306093808.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.12/MOD14.A2015285.0125.006.2015306093813.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.11/MOD14.A2015284.1435.006.2015306093623.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.11/MOD14.A2015284.1255.006.2015306093628.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.11/MOD14.A2015284.0225.006.2015306093151.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.11/MOD14.A2015284.0045.006.2015306093255.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.10/MOD14.A2015283.1350.006.2015306093405.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.10/MOD14.A2015283.0140.006.2015306090342.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.09/MOD14.A2015282.1445.006.2015306085138.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.09/MOD14.A2015282.1310.006.2015306085136.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.09/MOD14.A2015282.1305.006.2015306085138.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.09/MOD14.A2015282.0100.006.2015306085925.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.09/MOD14.A2015282.0055.006.2015306085944.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.08/MOD14.A2015281.1405.006.2015306084606.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.08/MOD14.A2015281.1400.006.2015306084155.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.08/MOD14.A2015281.0155.006.2015306083452.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.08/MOD14.A2015281.0150.006.2015306083510.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.07/MOD14.A2015280.1320.006.2015306101803.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.07/MOD14.A2015280.0110.006.2015306102127.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.06/MOD14.A2015279.1415.006.2015306100157.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.06/MOD14.A2015279.0205.006.2015306100353.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.06/MOD14.A2015279.0030.006.2015306100319.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.06/MOD14.A2015279.0025.006.2015306100345.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.05/MOD14.A2015278.1335.006.2015306100303.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.05/MOD14.A2015278.1330.006.2015306100356.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.05/MOD14.A2015278.0125.006.2015306100847.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.05/MOD14.A2015278.0120.006.2015306101020.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.04/MOD14.A2015277.1430.006.2015306092501.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.04/MOD14.A2015277.1425.006.2015306092502.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.04/MOD14.A2015277.0220.006.2015306093124.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.04/MOD14.A2015277.0215.006.2015306093147.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.04/MOD14.A2015277.0040.006.2015306093153.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.03/MOD14.A2015276.1345.006.2015306091822.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.03/MOD14.A2015276.0135.006.2015306092222.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.02/MOD14.A2015275.1440.006.2015306085206.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.02/MOD14.A2015275.1300.006.2015306085208.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.02/MOD14.A2015275.0055.006.2015306084823.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.02/MOD14.A2015275.0050.006.2015306084810.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.01/MOD14.A2015274.1400.006.2015306083544.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.01/MOD14.A2015274.1355.006.2015306083540.hdf
http://e4ftl01.cr.usgs.gov//MODV6_Dal_C/MOLT/MOD14.006/2015.10.01/MOD14.A2015274.0145.006.2015306083518.hdf

EDSCEOF
