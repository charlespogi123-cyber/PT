function simulateStatusChanges() {
    setInterval(() => {
        document.querySelectorAll('tr').forEach(row => {
            // Only affect devices that should randomly change status
            if(row.innerHTML.includes('FM-AP') || row.innerHTML.includes('FM-ASW02')) {
                const badge = row.querySelector('.badge');
                if(Math.random() > 0.7) { // 30% chance to toggle
                    if(badge.classList.contains('bg-success')) {
                        badge.className = 'badge bg-danger';
                        badge.innerHTML = '<i class="fas fa-times-circle"></i> OFFLINE';
                    } else {
                        badge.className = 'badge bg-success';
                        badge.innerHTML = '<i class="fas fa-check-circle"></i> ONLINE';
                    }
                }
            }
        });
    }, 10000); // Check every 10 seconds
}

// Start when page loads
document.addEventListener('DOMContentLoaded', simulateStatusChanges);