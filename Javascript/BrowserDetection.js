function detectBrowser() {
    const info = [
        { label: "Browser CodeName", value: navigator.appCodeName },
        { label: "Browser Name", value: navigator.appName },
        { label: "Browser Version", value: navigator.appVersion },
        { label: "Cookies Enabled", value: navigator.cookieEnabled },
        { label: "Browser Language", value: navigator.language },
        { label: "Browser Online", value: navigator.onLine },
        { label: "Platform", value: navigator.platform },
        { label: "User-agent", value: navigator.userAgent },
        { label: "Screen Resolution", value: `${window.screen.width}x${window.screen.height}` },
        { label: "Color Depth", value: `${window.screen.colorDepth}-bit` },
        { label: "Device Pixel Ratio", value: window.devicePixelRatio },
        { label: "Browser Vendor", value: navigator.vendor || "Unknown" }
    ];

    const demo = document.getElementById("demo");
    demo.innerHTML = info.map(item => `
        <div class="info-item">
            <span class="info-label">${item.label}:</span>
            <span class="info-value">${item.value}</span>
        </div>
    `).join('');
}

window.onload = detectBrowser;