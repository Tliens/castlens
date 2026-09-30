# -*- coding: utf-8 -*-
# CastLens SEO landing pages generator.
# Each page carries genuinely different content (unique sections + FAQs), not keyword swaps.
# Rebuild with: python3 scripts/gen_pages.py  (writes 4 HTML files + sitemap.xml)

import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://castlens.kuige.me"

PAGES = [
  # ------------------------------------------------------------------ 1
  {
    "slug": "private-screen-recorder",
    "title": {
      "en": "Private Screen Recorder — Nothing Leaves Your Device | CastLens",
      "zh": "私密录屏工具 — 画面不离设备 | CastLens"},
    "desc": {
      "en": "A screen recorder built so recordings cannot leak: no server, no upload endpoint, files go from browser memory straight to your disk. Verify it yourself.",
      "zh": "从架构上杜绝泄露的录屏工具：没有服务器、没有上传端点，文件从浏览器内存直接落盘。欢迎亲自验证。"},
    "h1": {
      "en": "A Screen Recorder That Can't Leak Your Recordings",
      "zh": "一台无法泄露你录屏的录屏机"},
    "intro": {
      "en": "Most \"online\" screen recorders are cloud pipelines: your screen is uploaded first, stored somewhere, then handed back to you as a link. CastLens inverts that. Recording happens inside your browser tab, the file is written straight to your disk, and there is no server on the other end — because the site doesn't have one.",
      "zh": "大多数「在线」录屏工具其实是云端流水线：你的屏幕先被上传、存到某处，再以链接形式还给你。CastLens 把这个流程倒过来了——录制发生在你的浏览器标签页里，文件直接写进你的硬盘，另一端没有服务器在接收——因为这个网站根本没有服务器。"},
    "sections": [
      {"h": {"en": "Why screen recordings leak", "zh": "录屏是怎么泄露的"},
       "p": {"en": "When a recorder uploads, three things can go wrong: the transfer itself (who sees it in transit), the storage (how long it sits there, who can read it), and access control (link guessing, sharing settings, breached accounts). Sensitive demos, unreleased products, customer data on screen — one mis-shared link and it's out. The only reliable fix is to never send the video anywhere in the first place.",
             "zh": "一旦录屏走上传链路，就有三个环节可能出事：传输本身（谁能在中途看到）、存储（存多久、谁能读）、访问控制（链接被猜到、分享设置错误、账号被盗）。未发布的产品、内部演示、屏幕上的客户数据——一个误分享的链接就全出去了。唯一可靠的解法，是从一开始就不把视频发往任何地方。"}},
      {"h": {"en": "How browser-local recording works", "zh": "浏览器本地录制的原理"},
       "p": {"en": "Modern browsers expose two standard APIs: getDisplayMedia() captures the screen into a live stream inside the page, and MediaRecorder encodes that stream in memory. When you press Download, the finished blob is written to a file. Between those steps there is no network hop — the video never becomes a request.",
             "zh": "现代浏览器提供两个标准 API：getDisplayMedia() 把屏幕捕获成页面内的实时流，MediaRecorder 在内存里编码这条流。你点下载时，成品 blob 才被写成文件。这几个步骤之间不存在任何网络跳转——视频从来不会变成一个网络请求。"}},
      {"h": {"en": "A 60-second trust test for any recorder", "zh": "给任何录屏工具做的 60 秒信任测试"},
       "p": {"en": "Before recording anything sensitive, open DevTools → Network, hit Record, and watch. A local recorder shows zero requests after page load. Then check the tool's privacy policy for words like \"processing\", \"retention\", and \"improve our services\" — each one means your video goes somewhere you don't control.",
             "zh": "录任何敏感内容前，打开开发者工具的 Network 面板，点开始录制，盯着看。本地工具在页面加载后请求数为零。再翻翻它的隐私政策，找「处理」「留存」「改进我们的服务」这类词——每一个都意味着你的视频去了你控制不了的地方。"}},
      {"h": {"en": "When private recording is the requirement", "zh": "什么时候必须用私密录屏"},
       "p": {"en": "Internal demos of unreleased features, bug reports containing user data, financial screens, medical or legal workflows, security-sensitive admin panels, and any company bound by NDAs or GDPR-style rules. If the content would be a problem in someone else's cloud, it should never touch a cloud.",
             "zh": "未发布功能的内部演示、含用户数据的缺陷报告、财务界面、医疗或法务流程、敏感的管理后台，以及所有受保密协议或 GDPR 类规则约束的公司。如果这段内容放在别人的云里会出问题，它就不该碰任何云。"}},
    ],
    "faqs": [
      {"q": {"en": "Does CastLens really never upload anything?", "zh": "CastLens 真的什么都不上传吗？"},
       "a": {"en": "Yes — it is a static page with no backend. The recording is produced and encoded inside your browser and saved directly by you. You can verify this with the browser's Network panel while recording.",
             "zh": "是的——它是纯静态页面，没有后端。录制的产生和编码都在你的浏览器内完成，由你自己保存。录制时打开浏览器的 Network 面板即可亲自验证。"}},
      {"q": {"en": "Can my employer or network admin see my recordings?", "zh": "我的雇主或网络管理员能看到我的录制吗？"},
       "a": {"en": "Not through CastLens — there is nothing to intercept because nothing is transmitted. What happens on a managed device is governed by your device policy (screen monitoring, disk encryption), which applies equally to any installed app.",
             "zh": "通过 CastLens 不能——没有传输就没有可截获的东西。受管设备上的情况由设备策略决定（屏幕监控、磁盘加密），这对任何本地安装的软件同样适用。"}},
      {"q": {"en": "Does it work offline?", "zh": "断网能用吗？"},
       "a": {"en": "Yes, after the page has loaded once. Recording, pausing, stopping, and saving all work with the network disconnected — which is itself proof that nothing is being uploaded.",
             "zh": "可以，页面加载过一次之后就行。录制、暂停、停止、保存在断网状态下全部可用——这本身就是不上传的证据。"}},
      {"q": {"en": "What happens to the video when I close the tab?", "zh": "关掉标签页后视频会怎样？"},
       "a": {"en": "It's gone. The unsaved recording exists only in the tab's memory. Unless you pressed Download, no copy exists anywhere — on this site or any other.",
             "zh": "消失了。未保存的录制只存在于标签页内存里。只要没点过下载，任何地方——本站或其他任何地方——都不存在副本。"}},
      {"q": {"en": "Is a browser recorder as private as an installed app?", "zh": "浏览器录屏和本地安装的软件一样私密吗？"},
       "a": {"en": "For recording privacy, yes — both capture and encode locally. An installed app additionally works without loading a website first; a browser tool has the advantage of zero install and nothing left on the machine afterwards. Pick based on workflow, not privacy.",
             "zh": "就录制隐私而言是一样的——两者都在本地捕获和编码。本地软件的额外好处是无需先加载网站；浏览器工具的优势是零安装、事后机器上不留痕。按工作流选就好，隐私上没有差别。"}},
    ],
  },
  # ------------------------------------------------------------------ 2
  {
    "slug": "screen-recorder-no-upload",
    "title": {
      "en": "Screen Recorder With No Upload — Record Straight to a File | CastLens",
      "zh": "无上传录屏 — 直接录成文件 | CastLens"},
    "desc": {
      "en": "Record your screen and get the video file immediately — no uploading, no waiting for cloud processing, no storage limits. MP4/WebM straight to your disk.",
      "zh": "录完立刻拿到视频文件——不上传、不等云端处理、没有存储限额。MP4/WebM 直接落盘。"},
    "h1": {
      "en": "Record Your Screen Without Uploading a Single Byte",
      "zh": "录屏，一个字节都不上传"},
    "intro": {
      "en": "Upload-based recorders make you wait: the video climbs to their cloud, gets processed, and comes back as a link with a quota attached. CastLens skips all of it — press Stop and the finished MP4 (or WebM) is on your desk in the same second. No progress bars for uploads that shouldn't exist.",
      "zh": "基于上传的录屏工具总让你等：视频先传上他们的云、等处理、再以带配额的链接还给你。CastLens 把这些全省了——点停止的那一刻，成品 MP4（或 WebM）已经落在你手里。不该存在的上传进度条，一根都没有。"},
    "sections": [
      {"h": {"en": "The upload math nobody mentions", "zh": "没人提的上传账"},
       "p": {"en": "A 10-minute 1080p recording is roughly 80–200 MB. On a typical 20 Mbps upstream, uploading that takes 1–2 minutes before processing even starts — every single time. Local recording costs zero seconds, zero bandwidth, and works identically on hotel Wi-Fi or a plane.",
             "zh": "10 分钟的 1080p 录制约 80–200 MB。按 20 Mbps 上行算，光是上传就要 1–2 分钟，处理还没开始——而且每次都这样。本地录制零秒、零带宽，在酒店 Wi-Fi 和飞机上同样好使。"}},
      {"h": {"en": "You own the file from the first frame", "zh": "从第一帧起文件就是你的"},
       "p": {"en": "Because the recording is encoded on your device, there is no account, no retention window, and no \"we may access recordings to improve our services\" clause to worry about. Move it, rename it, edit it, delete it — it's a normal file in your Downloads folder, in standard MP4 or WebM that every editor accepts.",
             "zh": "编码发生在你的设备上，所以没有账号、没有留存期、也不用担心「我们可能访问录制内容以改进服务」这类条款。移动、改名、剪辑、删除——它就是你下载文件夹里的普通文件，标准 MP4 或 WebM 格式，任何剪辑软件都认。"}},
      {"h": {"en": "Sharing stays on your terms", "zh": "分享方式由你决定"},
       "p": {"en": "No forced share links means you choose the channel: drag the file into WeChat or Slack, attach it to an email, upload it to the platform you pick — or don't send it at all. The recorder's job ends at producing a clean file, not at distributing your video through someone else's funnel.",
             "zh": "不强制生成分享链接，意味着渠道由你选：拖进微信或 Slack、附在邮件里、传到你自己挑的平台——或者压根不发。录屏工具的职责到产出一个干净文件为止，而不是把你的视频从别人的漏斗里分发出去。"}},
      {"h": {"en": "What no-upload doesn't mean", "zh": "「无上传」不代表什么"},
       "p": {"en": "It doesn't mean lower quality — resolution and frame rate come from your screen and CPU, not from a server plan. It also doesn't mean no cloud convenience: if you want a share link, upload the file yourself to whichever service you already trust. The difference is that it's your decision, made per recording.",
             "zh": "不代表画质妥协——分辨率和帧率取决于你的屏幕和 CPU，不取决于服务器套餐。也不代表放弃云便利：想要分享链接，把文件自己传到任何你信任的服务就行。区别在于：这是你按次自主做的决定。"}},
    ],
    "faqs": [
      {"q": {"en": "Is it really free of upload, or free-until-5-minutes?", "zh": "是真的无上传，还是「5 分钟内免费」那种？"},
       "a": {"en": "Really none. There is no length cap tied to upload because there is no upload — record an hour if your disk has room. Free here means free of the whole cloud pipeline.",
             "zh": "真的没有。上传都不存在，自然没有跟上传绑定的时长限制——硬盘有空间就录一小时也没问题。这里的免费，是整条云端流水线的免费。"}},
      {"q": {"en": "Can I record long meetings offline-style?", "zh": "长时间会议也能这样录吗？"},
       "a": {"en": "Yes. At typical settings expect roughly 40–100 MB per 10 minutes of 1080p. For hour-long sessions consider 720p, and use Pause during breaks — paused time produces no frames and no file size.",
             "zh": "可以。按典型设置，1080p 每 10 分钟约 40–100 MB。一小时的场次建议用 720p，休息时用暂停——暂停期间不产生帧，也不产生体积。"}},
      {"q": {"en": "What format do I get?", "zh": "拿到的是什么格式？"},
       "a": {"en": "MP4 (H.264) on Chrome 126+, Edge and Safari — ready for every platform. Firefox produces WebM, which major platforms accept; convert once if a specific tool demands MP4.",
             "zh": "Chrome 126+、Edge、Safari 上是 MP4（H.264），全平台通吃。Firefox 产出 WebM，主流平台都接受；个别工具非要 MP4 的话转一次即可。"}},
      {"q": {"en": "Why is there no share link feature?", "zh": "为什么没有分享链接功能？"},
       "a": {"en": "Because a share link requires storing your video on a server, which is exactly what this tool is built to avoid. Export the file and share it through whatever channel you already use — that keeps control on your side.",
             "zh": "因为分享链接意味着把你的视频存在服务器上，而这正是这个工具要避免的。导出文件、走你已有的渠道分享——控制权就始终在你手里。"}},
      {"q": {"en": "Does local recording limit quality or length?", "zh": "本地录制会限制画质或时长吗？"},
       "a": {"en": "No server plan caps anything here. Quality is bounded by your machine: screen resolution, chosen region size, and CPU for encoding. Length is bounded only by available disk space.",
             "zh": "没有服务器套餐来设限。上限只来自你的机器：屏幕分辨率、选区大小、编码用 CPU。时长只受磁盘剩余空间限制。"}},
    ],
  },
  # ------------------------------------------------------------------ 3
  {
    "slug": "screen-recorder-for-mac",
    "title": {
      "en": "Screen Recorder for Mac — Browser-Based, No App Install | CastLens",
      "zh": "Mac 录屏工具 — 浏览器直接录，无需装 App | CastLens"},
    "desc": {
      "en": "Free screen recorder for macOS: works in Chrome and Safari, supports region capture, webcam overlay and system audio. Covers the macOS screen-recording permission step by step.",
      "zh": "macOS 免费录屏：Chrome 与 Safari 可用，支持区域录制、摄像头画中画与系统声音。macOS 屏幕录制授权一步步讲清。"},
    "h1": {
      "en": "Screen Recorder for Mac — In the Browser, Nothing to Install",
      "zh": "Mac 录屏，就在浏览器里，什么都不用装"},
    "intro": {
      "en": "macOS already has QuickTime, and OBS is free — so why a browser recorder? Because for the 30-second job (\"record this tab, send the file\"), opening a URL beats setting up an app. Region selection, webcam overlay, pause & resume and trim come along for free, and nothing stays installed when you're done.",
      "zh": "macOS 有 QuickTime，OBS 也免费——为什么还要浏览器录屏？因为「录一下这个标签页、发个文件」这种 30 秒的活，开个网址比配置一个 App 划算得多。区域选择、摄像头画中画、暂停续录、一键裁剪全都带着，用完机器上不留任何安装。"},
    "sections": [
      {"h": {"en": "The one setup step: Screen Recording permission", "zh": "唯一的设置步骤：屏幕录制授权"},
       "p": {"en": "macOS requires you to grant Screen Recording to the browser itself, once. When you first record, the system asks; if that prompt was ever dismissed, macOS stays silent forever and captures fail quietly. Fix: System Settings → Privacy & Security → Screen Recording → enable your browser (toggle off/on if it looks enabled), then fully quit and reopen it — the grant only applies to freshly started apps.",
             "zh": "macOS 要求给浏览器本身授一次「屏幕录制」权限。首次录制时系统会询问；但如果那次弹窗被忽略，macOS 会永远沉默、捕获静默失败。修法：系统设置 → 隐私与安全性 → 屏幕录制 → 打开你的浏览器（看着已开就关掉再开一次），然后完全退出并重开浏览器——授权只对全新启动的进程生效。"}},
      {"h": {"en": "Audio on macOS: the honest matrix", "zh": "macOS 上的声音：一张诚实的对照表"},
       "p": {"en": "Tab audio always works — share a Chrome tab and its sound is captured. Whole-system audio needs Chrome 141+ on macOS 14.2+ (choose \"Entire screen\" and enable audio in the picker). Safari records the screen with microphone; full system audio there still needs a virtual audio device. Windows has none of these wrinkles.",
             "zh": "标签页声音永远可用——共享 Chrome 标签页即带声音。整系统声音需要 Chrome 141+ 且 macOS 14.2+（选「整个屏幕」并在选择器里勾选声音）。Safari 可以屏幕+麦克风；要整系统声音仍需虚拟声卡。Windows 没有这些讲究。"}},
      {"h": {"en": "Retina, regions and the floating console", "zh": "Retina、区域与悬浮控制台"},
       "p": {"en": "On Retina displays the capture is full-resolution; the region selector works in source pixels, so a \"1000×600\" region is exactly that in the output file. While you draw the region, a small always-on-top window floats above your actual screen — you frame the real content, then record, pause and stop from that same floating panel without coming back to the website.",
             "zh": "Retina 屏上捕获是全分辨率的；区域选择器按源像素工作，「1000×600」的框在成品里就是这个尺寸。画选区时，一个置顶小窗浮在你真实屏幕上方——对着真实内容取景，之后录制、暂停、停止都在这个悬浮面板里完成，不用切回网站。"}},
      {"h": {"en": "When to use QuickTime, OBS, or this", "zh": "什么时候用 QuickTime、OBS、或它"},
       "p": {"en": "QuickTime: zero features, always there, fine for full-screen-only captures. OBS: scenes, overlays, streaming — worth its setup time when you do that regularly. A browser recorder: fastest path from \"I need this recorded\" to a trimmed file, with nothing installed afterwards. Most Mac users need the third one 90% of the time.",
             "zh": "QuickTime：零功能、永远在，只录全屏凑合够用。OBS：场景、叠加层、直播——常干这些的人值得配置。浏览器录屏：从「我要录一下」到拿到裁好的文件的最快路径，事后零安装。大多数 Mac 用户 90% 的场景要的是第三个。"}},
    ],
    "faqs": [
      {"q": {"en": "Does it work in Safari on Mac?", "zh": "Mac 的 Safari 能用吗？"},
       "a": {"en": "Yes — Safari supports screen recording via the same standard API, outputs MP4, and needs the same one-time Screen Recording permission. Chrome and Edge work equally well; Firefox on macOS saves WebM.",
             "zh": "可以——Safari 支持同一套标准录屏 API，产出 MP4，同样只需一次性屏幕录制授权。Chrome 和 Edge 同样好用；macOS 上的 Firefox 存 WebM。"}},
      {"q": {"en": "Why is my DRM video (Netflix, etc.) recorded black?", "zh": "为什么录 Netflix 这类 DRM 视频是黑屏？"},
       "a": {"en": "Content protection intentionally blocks capture of protected video paths — this applies to every recorder on macOS, including OBS and QuickTime. Non-DRM content (your own apps, tabs, most sites) records normally.",
             "zh": "内容保护机制有意阻断受保护视频通路的捕获——macOS 上所有录屏工具都一样，包括 OBS 和 QuickTime。非 DRM 内容（你自己的应用、标签页、大多数网站）都正常录。"}},
      {"q": {"en": "How do I fix \"recording fails silently\" on macOS?", "zh": "macOS 上「静默录不上」怎么修？"},
       "a": {"en": "That's the permission quirk: macOS asks once and never re-prompts. Toggle the browser's Screen Recording switch off and on in System Settings → Privacy & Security, then fully quit (⌘Q) and reopen the browser. This site detects the failure and walks you through it.",
             "zh": "这就是那个授权怪癖：macOS 只问一次、不再重弹。到 系统设置 → 隐私与安全性 把浏览器的屏幕录制开关关掉再打开，然后 ⌘Q 完全退出并重开浏览器。本站检测到这种失败时会一步步引导你修。"}},
      {"q": {"en": "Is Retina quality preserved?", "zh": "Retina 画质有损失吗？"},
       "a": {"en": "Yes. Capture runs at the display's native resolution, and region sizes are exact in output pixels — a 1440×900 region on a 2× display yields a 1440×900 video (crisp, since the source was 2880×1800).",
             "zh": "没有。捕获按显示器原生分辨率进行，区域尺寸在成品里逐像素精确——2× 屏上选 1440×900，成品就是 1440×900（源是 2880×1800，所以非常锐利）。"}},
      {"q": {"en": "Does it work on Apple Silicon?", "zh": "Apple 芯片的 Mac 能用吗？"},
       "a": {"en": "Yes, M-series and Intel Macs behave identically — encoding uses the same MediaRecorder pipeline Chrome provides on both. Hardware encoding keeps fan noise low on M-chips even at 1080p30.",
             "zh": "可以，M 系列和 Intel Mac 行为一致——两者都用 Chrome 提供的同一套 MediaRecorder 管线。M 芯片上硬件编码让 1080p30 也几乎不转风扇。"}},
    ],
  },
  # ------------------------------------------------------------------ 4
  {
    "slug": "screen-recorder-with-audio",
    "title": {
      "en": "Screen Recorder With Audio — Mic, System Sound, or Both | CastLens",
      "zh": "带声音的录屏 — 麦克风、系统声或两者都要 | CastLens"},
    "desc": {
      "en": "Record your screen with audio: microphone narration, system or tab sound, or both mixed together. Plain-English guide to what works on Windows, macOS and each browser.",
      "zh": "录屏带声音：麦克风解说、系统或标签页声音、或两者混录。Windows/macOS/各浏览器支持情况讲清楚。"},
    "h1": {
      "en": "Record Your Screen with Audio — Mic, System Sound, or Both",
      "zh": "录屏带声音 — 麦克风、系统声，或者都要"},
    "intro": {
      "en": "Audio is where most screen recorders get confusing — permission dialogs, \"no system audio on macOS\" footnotes, muted surprises after upload. This guide covers the three ways to record sound with your screen, what each browser and OS actually supports today, and how to fix the common failures before they happen.",
      "zh": "声音是录屏工具最容易让人糊涂的地方——权限弹窗、「macOS 录不了系统声」的脚注、录完发现是哑巴的意外。这份指南讲清屏幕+声音的三种录法、各浏览器与系统今天的真实支持情况，以及如何提前排掉常见的坑。"},
    "sections": [
      {"h": {"en": "The three audio modes", "zh": "三种声音模式"},
       "p": {"en": "Mic only: your narration over the screen — works everywhere, ideal for tutorials and feedback. System/tab audio: the sound the computer plays — great for demoing apps, sites, or games. Both: CastLens mixes microphone and system sound into one track through the Web Audio API, so one file carries your voice and the app's audio together.",
             "zh": "仅麦克风：屏幕配你的解说——处处可用，适合教程和反馈。系统/标签页声音：电脑自己播的声音——适合演示应用、网站、游戏。两者都要：CastLens 通过 Web Audio 把麦克风和系统声混成一条音轨，一个文件同时带你的声音和应用的声音。"}},
      {"h": {"en": "What each platform actually supports", "zh": "各平台的真实支持情况"},
       "p": {"en": "Windows: full system audio in every Chromium browser — pick \"Entire screen\" and enable audio. macOS: tab audio always; whole-system audio on Chrome 141+ with macOS 14.2+ (older combos need a tab or a virtual audio device). Safari: screen + microphone. Firefox: tab and window audio where the platform allows. When a browser can't provide system audio, this recorder tells you immediately instead of delivering a silent file.",
             "zh": "Windows：所有 Chromium 浏览器都支持完整系统声——选「整个屏幕」并开启声音即可。macOS：标签页声音永远可录；整系统声需 Chrome 141+ 且 macOS 14.2+（旧组合要用标签页或虚拟声卡）。Safari：屏幕+麦克风。Firefox：视平台而定支持标签页/窗口声音。当浏览器给不出系统声时，本工具会当场告知，而不是给你一个哑巴文件。"}},
      {"h": {"en": "Recording a clean voiceover", "zh": "录一段干净的解说"},
       "p": {"en": "Use the 3-second countdown to settle before speaking, keep the mic 15–25 cm away, and do a 5-second test recording to check levels — your voice should peak clearly without clipping. Pause during mistakes instead of stopping: paused time costs nothing, and the built-in trimmer removes any rough start or ending afterwards.",
             "zh": "用 3 秒倒计时稳住再开口，麦克风保持 15–25 厘米距离，先录 5 秒测试看看电平——声音应清晰有峰值但不破音。讲错了用暂停而不是停止：暂停不产生任何体积，录完再用内置裁剪掐头去尾。"}},
      {"h": {"en": "Fixing silent recordings", "zh": "修好没声音的录制"},
       "p": {"en": "Silent system audio on Mac → share a Chrome tab instead of the screen, or update to Chrome 141+. Silent mic → check the browser's site-permission for the microphone and the OS input device. Audio present but badly synced → avoid recording through Bluetooth headsets, whose codecs add latency; a wired mic keeps lips and voice aligned.",
             "zh": "Mac 系统声无声 → 改共享 Chrome 标签页，或升级到 Chrome 141+。麦克风无声 → 检查浏览器站点麦克风权限和系统输入设备。有声但不同步 → 别用蓝牙耳机录，它的编解码会加延迟；有线麦克风能让口型和声音对齐。"}},
    ],
    "faqs": [
      {"q": {"en": "Can I record microphone and system audio at the same time?", "zh": "麦克风和系统声能同时录吗？"},
       "a": {"en": "Yes — enable both switches before starting. Both sources are mixed into a single audio track in the exported file, with the microphone's echo cancellation on by default.",
             "zh": "可以——开始前把两个开关都打开。两个声源会混进导出文件的同一条音轨，麦克风默认开启回声消除。"}},
      {"q": {"en": "Why can't I get system audio on my Mac?", "zh": "为什么我的 Mac 录不到系统声？"},
       "a": {"en": "Either the browser or macOS is older than Chrome 141 / macOS 14.2, or the picker's audio option wasn't enabled. Sharing a Chrome tab always captures the tab's sound regardless of versions — the reliable fallback.",
             "zh": "要么浏览器/macOS 版本低于 Chrome 141 / macOS 14.2，要么选择器里没勾声音选项。共享 Chrome 标签页在任何版本下都能录到标签页声音——这是最可靠的退路。"}},
      {"q": {"en": "Which audio format does the recording use?", "zh": "录制的音频是什么格式？"},
       "a": {"en": "MP4 output carries AAC; WebM output carries Opus — both standard, accepted by every editor and platform. No exotic codecs, nothing to install.",
             "zh": "MP4 里是 AAC，WebM 里是 Opus——都是标准格式，所有剪辑软件和平台都收。没有冷门编解码，无需安装任何东西。"}},
      {"q": {"en": "Can I remove audio or keep video only?", "zh": "能去掉声音只留画面吗？"},
       "a": {"en": "Simply leave both audio switches off before recording — you get a clean video-only file. Recording video-only also slightly reduces file size and CPU load.",
             "zh": "录制前把两个声音开关都关掉就行——得到纯净的纯视频文件。纯视频还会略降体积和 CPU 占用。"}},
      {"q": {"en": "Does trimming affect the audio sync?", "zh": "裁剪会影响音画同步吗？"},
       "a": {"en": "No. The built-in trimmer re-encodes video and audio on the same timeline, cutting both tracks at your chosen in/out points, so sync is preserved to the frame.",
             "zh": "不会。内置裁剪在同一时间线上重编码视频和音频，两条轨按你选的入出点同时裁切，同步精确到帧。"}},
    ],
  },
]

CSS = """:root{--bg:#faf6ee;--card:#fffdf8;--ink:#2b2320;--mut:#7a6f66;--accent:#bc4b2c;--line:rgba(43,35,32,.13)}
html.dark{--bg:#171210;--card:#211a15;--ink:#f0e8dd;--mut:#a89a8c;--accent:#e06a45;--line:rgba(240,232,221,.13)}
*{box-sizing:border-box}[hidden]{display:none!important}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB',sans-serif;background:var(--bg);color:var(--ink);line-height:1.7;transition:background .25s,color .25s}
.wrap{max-width:820px;margin:0 auto;padding:0 20px}
.top{position:sticky;top:0;z-index:10;background:color-mix(in srgb,var(--bg) 85%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line))}
.top .wrap{display:flex;align-items:center;gap:12px;height:54px}
.brand{font-weight:700;font-size:16px;color:var(--ink);text-decoration:none}
.kuige-entry{color:var(--mut);text-decoration:none;font-size:13px;padding:4px 10px;border:1px solid var(--line);border-radius:99px;margin-left:auto}
.kuige-entry:hover{color:var(--accent);border-color:var(--accent)}
.langbtn{background:none;border:1px solid var(--line);border-radius:9px;color:var(--mut);font-size:13px;padding:4px 10px;cursor:pointer}
.langbtn:hover{color:var(--accent);border-color:var(--accent)}
.hero{padding:52px 0 8px}
.eyebrow{font-size:12.5px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--accent);margin:0 0 10px}
h1{font-size:clamp(26px,4.6vw,38px);line-height:1.25;margin:0 0 14px;letter-spacing:-.4px}
.lead{font-size:16.5px;color:var(--mut);max-width:640px;margin:0 auto}
.cta{display:inline-block;margin-top:22px;background:var(--accent);color:#fff;text-decoration:none;font-weight:600;font-size:15.5px;padding:13px 30px;border-radius:12px}
.cta:hover{filter:brightness(1.08)}
.blk{padding:34px 0 4px}
h2{font-size:21px;margin:0 0 10px}
.blk p{color:var(--mut);font-size:15px;margin:0 0 6px;text-align:left}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:18px}
details{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin-bottom:10px}
summary{cursor:pointer;font-weight:600;font-size:15px}
details p{color:var(--mut);font-size:14px;margin:10px 0 0}
.rel{display:flex;gap:10px;flex-wrap:wrap;padding:6px 0 10px}
.rel a{color:var(--mut);text-decoration:none;border:1px solid var(--line);border-radius:99px;padding:6px 14px;font-size:13px}
.rel a:hover{color:var(--accent);border-color:var(--accent)}
footer{border-top:1px solid var(--line);margin-top:44px;padding:24px 0 32px;text-align:center;color:var(--mut);font-size:13px}
footer a{color:var(--mut)}
.hero,.blk,.rel,footer .cn{text-align:center}"""

SWITCH_JS = """(function(){
  var q = new URLSearchParams(location.search).get('lang');
  var saved = null; try{ saved = localStorage.getItem('castlens-lang'); }catch(e){}
  var lang = q || saved || ((navigator.language||'en').toLowerCase().indexOf('zh')===0 ? 'zh' : 'en');
  var META = {};
  function apply(l){
    lang = (l === 'zh') ? 'zh' : 'en';
    document.documentElement.lang = lang;
    document.title = META.title[lang];
    var md = document.querySelector('meta[name="description"]');
    if (md) md.setAttribute('content', META.desc[lang]);
    document.querySelectorAll('[data-zh]').forEach(function(el){
      var cur = el.textContent, zh = el.getAttribute('data-zh');
      if (lang === 'zh'){ el.setAttribute('data-en', cur); el.textContent = zh; }
      else { var en = el.getAttribute('data-en'); if (en != null) el.textContent = en; }
    });
    var b = document.getElementById('langBtn');
    if (b) b.textContent = (lang === 'en') ? '中文' : 'EN';
    try{ localStorage.setItem('castlens-lang', lang); }catch(e){}
    var u = new URL(location.href);
    if (lang === 'zh') u.searchParams.set('lang','zh'); else u.searchParams.delete('lang');
    history.replaceState(null, '', u);
  }
  window.__applyLang = apply;
  document.getElementById('langBtn').addEventListener('click', function(){ apply(lang === 'en' ? 'zh' : 'en'); });
  window.__setMeta = function(t, d){ META.title = t; META.desc = d; apply(q || saved || ((navigator.language||'en').toLowerCase().indexOf('zh')===0 ? 'zh' : 'en')); };
})();"""

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

def bi(el, attr, en, zh):
    return '<%s %s="%s">%s</%s>' % (el, attr, esc(zh), esc(en), el)

def build_page(pg):
    slug = pg["slug"]
    url = BASE + "/" + slug + "/"
    en, zh = pg["title"]["en"], pg["title"]["zh"]
    den, dzh = pg["desc"]["en"], pg["desc"]["zh"]

    related = [p for p in PAGES if p["slug"] != slug]
    rel_html = "".join('<a href="/%s/" data-zh="%s">%s</a>' % (p["slug"], esc(p["navlabel"]["zh"]), esc(p["navlabel"]["en"])) for p in related)

    secs = []
    for s in pg["sections"]:
        secs.append('      <div class="card">\n        <h2 %s>%s</h2>\n        <p %s>%s</p>\n      </div>' % (
            bi_frag("data-zh", s["h"]["zh"]), esc(s["h"]["en"]),
            bi_frag("data-zh", s["p"]["zh"]), esc(s["p"]["en"])))
    faqs = []
    for f in pg["faqs"]:
        faqs.append('      <details><summary %s>%s</summary><p %s>%s</p></details>' % (
            bi_frag("data-zh", f["q"]["zh"]), esc(f["q"]["en"]),
            bi_frag("data-zh", f["a"]["zh"]), esc(f["a"]["en"])))

    ld_faq = json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": f["q"]["en"],
                        "acceptedAnswer": {"@type": "Answer", "text": f["a"]["en"]}} for f in pg["faqs"]]},
        ensure_ascii=False)
    ld_page = json.dumps({"@context": "https://schema.org", "@type": "WebPage",
        "name": en, "url": url, "description": den, "inLanguage": "en",
        "isPartOf": {"@type": "WebSite", "name": "CastLens", "url": BASE + "/"}},
        ensure_ascii=False)

    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_en}</title>
<meta name="description" content="{desc_en}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="zh" href="{url}?lang=zh">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="CastLens">
<meta property="og:title" content="{title_en}">
<meta property="og:description" content="{desc_en}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{base}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title_en}">
<meta name="twitter:description" content="{desc_en}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='13' fill='%231a1512'/%3E%3Crect x='12' y='16' width='40' height='28' rx='4' fill='none' stroke='%23e06a45' stroke-width='3'/%3E%3Ccircle cx='32' cy='30' r='7' fill='%23e06a45'/%3E%3C/svg%3E">
<script type="application/ld+json">{ld_page}</script>
<script type="application/ld+json">{ld_faq}</script>
<style>{css}</style>
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="/">▣ CastLens</a>
  <a class="kuige-entry" href="https://kuige.me/" target="_blank" rel="noopener" title="kuige.me" style="text-decoration:none">魁歌 · 独立开发者</a>
  <button class="langbtn" id="langBtn">中文</button>
</div></header>
<main class="wrap">
  <section class="hero">
    <p class="eyebrow" data-zh="免费在线录屏">Free Online Screen Recorder</p>
    <h1 data-zh="{h1_zh}">{h1_en}</h1>
    <p class="lead" data-zh="{intro_zh}">{intro_en}</p>
    <a class="cta" href="/" data-zh="打开 CastLens 开始录制">Open CastLens and record now</a>
  </section>
  <section class="blk">
{secs}
  </section>
  <section class="blk">
    <h2 data-zh="常见问题">FAQ</h2>
{faqs}
  </section>
  <section class="blk">
    <h2 data-zh="相关指南">Related guides</h2>
    <div class="rel">{rel}</div>
  </section>
</main>
<footer>
  <div class="wrap">
    <p class="cn">本站代号：画壁 — 壁上作画，画中人动；屏幕即画壁，帧帧入片。</p>
    <p><a href="/">CastLens</a> · © 2026 魁歌 KuiGe</p>
  </div>
</footer>
<script>
{switch_js}
__setMeta({{ "en": {title_en_j}, "zh": {title_zh_j} }}, {{ "en": {desc_en_j}, "zh": {desc_zh_j} }});
</script>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "948f2535a9dd4775a436c677b3c950e4"}}'></script>
</body>
</html>
""".format(
        title_en=esc(en), desc_en=esc(den), url=url, base=BASE,
        h1_en=esc(pg["h1"]["en"]), h1_zh=esc(pg["h1"]["zh"]),
        intro_en=esc(pg["intro"]["en"]), intro_zh=esc(pg["intro"]["zh"]),
        secs="\n".join(secs), faqs="\n".join(faqs), rel=rel_html,
        ld_page=ld_page, ld_faq=ld_faq, css=CSS, switch_js=SWITCH_JS,
        title_en_j=json.dumps(en, ensure_ascii=False), title_zh_j=json.dumps(zh, ensure_ascii=False),
        desc_en_j=json.dumps(den, ensure_ascii=False), desc_zh_j=json.dumps(dzh, ensure_ascii=False),
    )

def bi_frag(attr, zh):
    return '%s="%s"' % (attr, esc(zh))

def build_sitemap():
    urls = [(BASE + "/", 1.0), (BASE + "/?lang=zh", 0.8)]
    for pg in PAGES:
        urls.append((BASE + "/" + pg["slug"] + "/", 0.9))
        urls.append((BASE + "/" + pg["slug"] + "/?lang=zh", 0.7))
    entries = []
    today = "2026-09-30"
    for loc, pri in urls:
        entries.append("""  <url>
    <loc>%s</loc>
    <xhtml:link rel="alternate" hreflang="en" href="%s"/>
    <xhtml:link rel="alternate" hreflang="zh" href="%s?lang=zh"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>
    <lastmod>%s</lastmod>
    <priority>%.1f</priority>
  </url>""" % (loc, loc.rstrip('/') + '/', loc.rstrip('/') + '/', loc.rstrip('/') + '/', today, pri))
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(entries) + "\n</urlset>\n"

# nav labels for cross-links
NAVLABELS = {
    "private-screen-recorder": {"en": "Private screen recorder", "zh": "私密录屏"},
    "screen-recorder-no-upload": {"en": "Screen recorder, no upload", "zh": "无上传录屏"},
    "screen-recorder-for-mac": {"en": "Screen recorder for Mac", "zh": "Mac 录屏指南"},
    "screen-recorder-with-audio": {"en": "Screen recorder with audio", "zh": "带声音的录屏"},
}
for pg in PAGES:
    pg["navlabel"] = NAVLABELS[pg["slug"]]

if __name__ == "__main__":
    for pg in PAGES:
        d = os.path.join(ROOT, pg["slug"])
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, "index.html")
        open(path, "w", encoding="utf-8").write(build_page(pg))
        print("wrote", path, os.path.getsize(path), "bytes")
    sm = os.path.join(ROOT, "sitemap.xml")
    open(sm, "w", encoding="utf-8").write(build_sitemap())
    print("wrote", sm)
