// System Alerts & Global Announcements Logic
document.addEventListener('DOMContentLoaded', () => {
    initSystemAlerts();
    initAdminPreview();
});

function initSystemAlerts() {
    const announcementStr = localStorage.getItem('bi_active_announcement');
    if (!announcementStr) return;

    try {
        const announcement = JSON.parse(announcementStr);
        if (!announcement.active) return;

        const dismissedStr = localStorage.getItem('bi_dismissed_announcements') || '[]';
        const dismissed = JSON.parse(dismissedStr);
        
        // Show everywhere unless dismissed
        if (dismissed.includes(announcement.id)) return;

        showBanner(announcement);
    } catch (e) {
        console.error('Error parsing announcement:', e);
    }
}

function initAdminPreview() {
    const previewBox = document.getElementById('active-broadcast-preview');
    if (!previewBox) return;

    const announcementStr = localStorage.getItem('bi_active_announcement');
    if (announcementStr) {
        try {
            const announcement = JSON.parse(announcementStr);
            if (announcement.active) {
                previewBox.classList.remove('hidden');
                
                let icon = '';
                if (announcement.type.includes('Kritisk')) icon = '🔴';
                else if (announcement.type.includes('Advarsel')) icon = '🟡';
                else if (announcement.type.includes('Feature')) icon = '🔵';

                const content = document.getElementById('active-broadcast-content');
                if (content) {
                    content.innerHTML = `<strong>${icon} ${announcement.title}</strong><br><span class="opacity-80 font-normal">${announcement.message}</span>`;
                }
            } else {
                previewBox.classList.add('hidden');
            }
        } catch(e) {
            previewBox.classList.add('hidden');
        }
    } else {
        previewBox.classList.add('hidden');
    }
}

function showBanner(announcement) {
    let bgColor = 'bg-deep-indigo'; // Default / Feature
    if (announcement.type.includes('Kritisk')) {
        bgColor = 'bg-rose-critical'; // Rose #E11D48
    } else if (announcement.type.includes('Advarsel')) {
        bgColor = 'bg-amber-600'; // Amber #D97706
    }

    const bannerHtml = `
        <div id="global-announcement-banner" class="${bgColor} text-white px-4 py-3 flex items-center justify-between z-50 w-full flex-shrink-0 relative shadow-md">
            <div class="flex-1 flex flex-col md:flex-row md:items-center gap-1 md:gap-3">
                <span class="font-bold text-sm flex items-center gap-2">
                    ${announcement.type.includes('Kritisk') ? '<span class="material-symbols-outlined text-[18px]">warning</span>' : ''}
                    ${announcement.type.includes('Advarsel') ? '<span class="material-symbols-outlined text-[18px]">info</span>' : ''}
                    ${announcement.type.includes('Feature') ? '<span class="material-symbols-outlined text-[18px]">new_releases</span>' : ''}
                    ${announcement.title}
                </span>
                <span class="text-sm opacity-90 block md:inline">
                    ${announcement.message}
                </span>
                ${announcement.linkUrl ? `
                <a href="${announcement.linkUrl}" class="text-xs font-semibold underline hover:text-white/80 transition-colors whitespace-nowrap mt-1 md:mt-0 md:ml-2">
                    ${announcement.linkText || 'Læs mere'}
                </a>` : ''}
            </div>
            <button onclick="dismissAnnouncement('${announcement.id}')" class="text-white/80 hover:text-white transition-colors p-1 rounded-full hover:bg-white/10 flex items-center justify-center ml-4 shrink-0">
                <span class="material-symbols-outlined text-[20px]">close</span>
            </button>
        </div>
    `;

    // Inject before the main layout container or topbar. In this layout, inject before everything in body.
    const body = document.body;
    body.insertAdjacentHTML('afterbegin', bannerHtml);
}

window.dismissAnnouncement = function(id) {
    const banner = document.getElementById('global-announcement-banner');
    if (banner) banner.remove();

    const dismissedStr = localStorage.getItem('bi_dismissed_announcements') || '[]';
    try {
        const dismissed = JSON.parse(dismissedStr);
        if (!dismissed.includes(id)) {
            dismissed.push(id);
            localStorage.setItem('bi_dismissed_announcements', JSON.stringify(dismissed));
        }
    } catch (e) {
        localStorage.setItem('bi_dismissed_announcements', JSON.stringify([id]));
    }
};

window.broadcastMessage = function(type, title, message, linkUrl, linkText) {
    const announcement = {
        id: 'msg_' + Date.now(),
        type,
        title,
        message,
        linkUrl,
        linkText,
        active: true,
        createdAt: new Date().toISOString()
    };
    localStorage.setItem('bi_active_announcement', JSON.stringify(announcement));
    location.reload(); 
};

window.recallMessage = function() {
    localStorage.removeItem('bi_active_announcement');
    location.reload();
};
