function toggleSubmenu(id) {
  const submenu = document.getElementById(id);
  if (submenu.classList.contains('submenu-visible')) {
    submenu.classList.remove('submenu-visible');
  } else {
    submenu.classList.add('submenu-visible');
  }
}
