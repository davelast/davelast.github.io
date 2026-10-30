(() => {
  'use strict';
  document.querySelectorAll('[data-copy]').forEach(button => {
    const source = document.getElementById(button.dataset.copy);
    const status = document.getElementById(button.getAttribute('aria-describedby'));
    if (!source || !status) return;
    button.hidden = false;
    button.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(source.textContent);
        status.textContent = 'Copied.';
      } catch {
        status.textContent = 'Select the template below to copy it, or use Download.';
        source.focus();
      }
    });
  });
})();
