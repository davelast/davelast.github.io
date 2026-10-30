(() => {
  'use strict';
  const toolbar = document.querySelector('.toolbar');
  const select = document.querySelector('#category');
  const counter = document.querySelector('#counter');
  const previous = document.querySelector('#previous');
  const next = document.querySelector('#next');
  const all = [...document.querySelectorAll('.example')];
  const groups = [...document.querySelectorAll('.example-group')];
  let visible = all;
  let current = 0;
  let scheduled = false;

  function update() {
    counter.textContent = `${current + 1} of ${visible.length}`;
    previous.disabled = current === 0;
    next.disabled = current === visible.length - 1;
    all.forEach(item => item.removeAttribute('aria-current'));
    visible[current].setAttribute('aria-current', 'true');
  }

  function measure() {
    // Select the last example whose top has reached the reading line.
    // This stays stable through tall mobile cards and the gaps between groups.
    const line = toolbar.getBoundingClientRect().bottom + 60;
    current = 0;
    visible.forEach((item, index) => {
      if (item.getBoundingClientRect().top <= line) current = index;
    });
    update();
    scheduled = false;
  }

  function queueMeasure() {
    if (!scheduled) { scheduled = true; requestAnimationFrame(measure); }
  }

  function applyFilter(value) {
    visible = all.filter(item => value === 'all' || item.dataset.category === value);
    all.forEach(item => { item.hidden = !visible.includes(item); });
    groups.forEach(group => { group.hidden = !visible.some(item => group.contains(item)); });
    current = 0;
    update();
  }

  function goTo(index) {
    current = Math.max(0, Math.min(index, visible.length - 1));
    const item = visible[current];
    history.replaceState(null, '', `#${item.id}`);
    // Immediate steps keep the controls responsive and avoid motion or
    // partially completed animations when the browser backgrounds the tab.
    item.scrollIntoView({ behavior:'instant', block:'start' });
    update();
  }

  function revealHash() {
    const item = all.find(item => `#${item.id}` === location.hash);
    if (!item) return;
    if (item.hidden) { select.value = 'all'; applyFilter('all'); }
    current = visible.indexOf(item);
    item.scrollIntoView({ behavior:'instant', block:'start' });
    update();
  }

  select.addEventListener('change', () => {
    applyFilter(select.value);
    goTo(0);
  });
  previous.addEventListener('click', () => goTo(current - 1));
  next.addEventListener('click', () => goTo(current + 1));
  addEventListener('scroll', queueMeasure, { passive:true });
  addEventListener('resize', queueMeasure);
  addEventListener('hashchange', revealHash);
  // Reload restoration and web-font layout can happen after deferred scripts.
  // Reposition explicit deep links once the final page geometry is ready.
  addEventListener('pageshow', () => requestAnimationFrame(revealHash));
  if (document.fonts) document.fonts.ready.then(revealHash);
  if ('ResizeObserver' in window) new ResizeObserver(() => {
    document.documentElement.style.setProperty('--toolbar-height', `${toolbar.offsetHeight}px`);
    queueMeasure();
  }).observe(toolbar);
  toolbar.hidden = false;
  select.value = 'all';
  update();
  revealHash();
  queueMeasure();
})();
