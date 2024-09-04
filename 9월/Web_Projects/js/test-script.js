function filterContent(category) {
    const filterText = document.getElementById('filter-text');
    
    if (category === 'All') {
        filterText.innerHTML = "HTML, CSS, JavaScript, React, Spring-boot, C, C++, C#, Python, MySQL, MongoDB, Azure, AWS";
    } else if (category === 'Front-end') {
        filterText.innerHTML = "Front-End Skills: HTML, CSS, JavaScript, React.";
    } else if (category === 'Back-end') {
        filterText.innerHTML = "Back-End Skills: Spring-boot, C, C++, C#, Python";
    } else if (category === 'Database') {
        filterText.innerHTML = "Database Skills: MySQL, MongoDB";
    } else if (category === 'Cloud') {
        filterText.innerHTML = "Cloud: Azure, AWS"
    }
}
