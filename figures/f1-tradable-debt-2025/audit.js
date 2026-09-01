// Inject before </body> and read document.title. "CELLFIT::CLEAN" means every
// cell's content fits its box. Anything else lists the offenders.
document.fonts.ready.then(() => {
  const bad = [];
  document.querySelectorAll('.cell,.tile').forEach(e => {
    if (e.scrollWidth > e.clientWidth + 1 || e.scrollHeight > e.clientHeight + 1)
      bad.push(`${e.className} "${(e.textContent || '').trim().slice(0, 20)}" `
        + `[${e.scrollWidth}x${e.scrollHeight} in ${e.clientWidth}x${e.clientHeight}]`);
  });
  document.title = 'CELLFIT::' + (bad.length ? bad.join(' || ') : 'CLEAN');
});
