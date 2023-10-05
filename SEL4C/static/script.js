document.addEventListener('DOMContentLoaded', () => {
    const menuItems = document.querySelectorAll('.menu-item');
    const submenuItems = document.querySelectorAll('.submenu-item');



    menuItems.forEach(item => {
        item.addEventListener('click', (e) => {
            // Evita que el evento se propague al hacer clic en el submenú
            e.stopPropagation();

            menuItems.forEach(el => el.classList.remove('active'));
            item.classList.add('active');
        });
    });

    submenuItems.forEach(subItem => {
        subItem.addEventListener('click', (e) => {
            e.stopPropagation();

            submenuItems.forEach(el => el.classList.remove('active'));
            subItem.classList.add('active');
        });
    });

    // Opcional: Cerrar submenús al hacer clic fuera
    document.body.addEventListener('click', () => {
        menuItems.forEach(el => el.classList.remove('active'));
    });
});


