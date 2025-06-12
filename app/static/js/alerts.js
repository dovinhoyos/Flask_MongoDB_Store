function confirmDelete(deleteUrl) {
  Swal.fire({
    title: "Eliminar Producto",
    text: "¿Está seguro de eliminar?",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "SI",
    cancelButtonText: "NO",
  }).then((result) => {
    if (result.isConfirmed) {
      const form = document.createElement("form");
      form.method = "POST";
      form.action = deleteUrl;
      document.body.appendChild(form);
      form.submit();
    }
  });
}
