function showContent(contentId) {
    // Hide all content
    const contentItems = document.querySelectorAll('.content-item');
    contentItems.forEach(item => item.classList.remove('active'));
  
    // Show the clicked content
    const contentToShow = document.getElementById(contentId);
    contentToShow.classList.add('active');
  }