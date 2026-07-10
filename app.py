<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vawvi Video Downloader</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-white flex flex-col min-h-screen font-sans text-gray-900">

    <!-- Navbar -->
    <nav class="max-w-6xl w-full mx-auto px-4 py-6 flex justify-between items-center">
        <h1 class="text-2xl font-bold text-gray-800 tracking-tight">Vawvi</h1>
        <div class="space-x-6 text-sm font-medium text-gray-600 hidden md:block">
            <a href="#" class="hover:text-gray-900 transition-colors">Home</a>
            <a href="#supported" class="hover:text-gray-900 transition-colors">Supported Sites</a>
            <a href="#" class="hover:text-gray-900 transition-colors">Contact</a>
        </div>
    </nav>

    <!-- Main Content Area -->
    <main class="flex-grow max-w-4xl w-full mx-auto px-4 text-center mt-16">
        <h2 class="text-5xl md:text-6xl font-extrabold text-[#1a2b3b] leading-tight mb-4">
            Download Any Video <br> Instantly.
        </h2>
        <p class="text-gray-500 text-lg mb-10">
            Fast, free, and secure video downloader by Vawvi. No registration required.
        </p>

        <!-- Input Area -->
        <div class="flex flex-col md:flex-row justify-center items-center gap-4 max-w-2xl mx-auto">
            <input type="text" id="videoUrl" placeholder="Paste video link here (YouTube, FB, Insta)..." 
                class="w-full md:w-3/4 px-4 py-4 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-[#06b6d4] shadow-sm text-base">
            <button id="downloadBtn" onclick="fetchVideo()" 
                class="w-full md:w-auto bg-[#06b6d4] hover:bg-[#0891b2] text-white font-bold py-4 px-8 rounded-lg transition-colors shadow-md flex items-center justify-center gap-2">
                Download
            </button>
        </div>

        <!-- Supported Platforms Badges -->
        <div id="supported" class="mt-8 flex flex-wrap justify-center items-center gap-4 text-sm font-medium text-gray-600">
            <span class="text-gray-400 mr-2">Supported Platforms:</span>
            
            <div class="flex items-center gap-1.5 bg-red-50 text-red-600 px-3 py-1.5 rounded-full border border-red-100">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
                YouTube
            </div>

            <div class="flex items-center gap-1.5 bg-pink-50 text-pink-600 px-3 py-1.5 rounded-full border border-pink-100">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>
                Instagram
            </div>

            <div class="flex items-center gap-1.5 bg-blue-50 text-blue-600 px-3 py-1.5 rounded-full border border-blue-100">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                Facebook
            </div>
        </div>
        
        <p id="statusMsg" class="text-[#06b6d4] text-sm mt-6 hidden font-medium">Fetching video... Please wait.</p>

        <!-- Result Card -->
        <div id="resultCard" class="hidden mt-10 p-4 border border-gray-200 rounded-xl shadow-lg max-w-2xl mx-auto bg-gray-50 flex-col md:flex-row items-center gap-6">
            
            <div class="w-full md:w-1/2 rounded-lg overflow-hidden bg-gray-200 aspect-video flex items-center justify-center">
                <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
            </div>

            <div class="w-full md:w-1/2 text-left flex flex-col gap-3">
                <h3 id="vidTitle" class="font-bold text-gray-800 text-lg line-clamp-2">Vawvi Ready Video</h3>
                
                <div>
                    <label class="text-xs text-gray-500 font-semibold uppercase tracking-wider">Resolution</label>
                    <select id="vidResolution" class="mt-1 w-full p-2.5 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-[#06b6d4] text-sm bg-white">
                        <option value="best">Best Quality (Auto)</option>
                        <option value="1080p">High Definition</option>
                        <option value="720p">Standard Quality</option>
                    </select>
                </div>

                <button onclick="triggerDownload(this)" class="mt-3 w-full bg-[#10b981] hover:bg-[#059669] text-white font-bold py-3 px-4 rounded-md transition-colors flex items-center justify-center gap-2 shadow-sm">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                    Save to Device
                </button>
            </div>
        </div>
    </main>

    <!-- Professional Footer -->
    <footer class="mt-20 border-t border-gray-200 bg-gray-50 py-8">
        <div class="max-w-6xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center text-gray-500 text-sm">
            <p>&copy; 2026 Vawvi. All rights reserved.</p>
            <div class="flex space-x-6 mt-4 md:mt-0 font-medium">
                <a href="#" class="hover:text-[#06b6d4] transition-colors">Privacy Policy</a>
                <a href="#" class="hover:text-[#06b6d4] transition-colors">Terms of Service</a>
                <a href="#" class="hover:text-[#06b6d4] transition-colors">Contact Support</a>
            </div>
        </div>
    </footer>

    <!-- Functionality Scripts -->
    <script>
        let currentDirectLink = "";
        let currentTitle = "";

        async function fetchVideo() {
            const urlInput = document.getElementById("videoUrl").value.trim();
            const statusMsg = document.getElementById("statusMsg");
            const resultCard = document.getElementById("resultCard");
            const downloadBtn = document.getElementById("downloadBtn");

            if (!urlInput) {
                alert("Bhai, pehle video ka link toh daalo!");
                return;
            }

            statusMsg.textContent = "Fetching video securely... Please wait.";
            statusMsg.classList.remove("hidden", "text-red-500");
            statusMsg.classList.add("text-[#06b6d4]");
            resultCard.classList.add("hidden");
            downloadBtn.disabled = true;
            downloadBtn.classList.add("opacity-50");

            try {
                // Request ja rahi hai tumhare khud ke Render server ko
                const apiUrl = `https://vawvi-video-api.onrender.com/api/extract?url=${encodeURIComponent(urlInput)}`;
                
                const response = await fetch(apiUrl);
                const data = await response.json();

                if (data.success) {
                    statusMsg.textContent = "Download ready!";
                    statusMsg.classList.replace("text-[#06b6d4]", "text-[#10b981]");
                    
                    currentDirectLink = data.direct_link;
                    currentTitle = data.title;

                    resultCard.classList.remove("hidden");
                    resultCard.classList.add("flex");
                } else {
                    throw new Error(data.error || "Failed to extract link");
                }
            } catch (error) {
                statusMsg.textContent = "Error: " + error.message;
                statusMsg.classList.replace("text-[#06b6d4]", "text-red-500");
            } finally {
                downloadBtn.disabled = false;
                downloadBtn.classList.remove("opacity-50");
            }
        }

        async function triggerDownload(btn) {
            if (!currentDirectLink) return;
            
            const originalText = btn.innerHTML;
            btn.innerHTML = "Downloading... Please wait";
            btn.disabled = true;
            btn.classList.add("opacity-75", "cursor-not-allowed");
            
            try {
                const response = await fetch(currentDirectLink);
                if (!response.ok) throw new Error("Network error");
                
                const blob = await response.blob();
                const blobUrl = window.URL.createObjectURL(blob);
                
                const a = document.createElement("a");
                a.href = blobUrl;
                a.download = currentTitle + ".mp4"; 
                document.body.appendChild(a);
                a.click();
                
                document.body.removeChild(a);
                window.URL.revokeObjectURL(blobUrl);
            } catch (error) {
                const a = document.createElement("a");
                a.href = currentDirectLink;
                a.download = currentTitle + ".mp4"; 
                a.target = "_blank"; 
                a.rel = "noopener noreferrer";
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            } finally {
                btn.innerHTML = originalText;
                btn.disabled = false;
                btn.classList.remove("opacity-75", "cursor-not-allowed");
            }
        }
    </script>
</body>
</html>
