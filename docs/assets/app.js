(function () {
  // プロンプトのコピー
  document.addEventListener('click', function (e) {
    var btn = e.target.closest ? e.target.closest('[data-copy]') : null;
    if (!btn) return;
    var pre = btn.closest('.prompt').querySelector('pre');
    var text = pre ? pre.innerText : '';
    function done(ok) {
      var old = btn.getAttribute('data-label') || btn.textContent;
      btn.setAttribute('data-label', old);
      btn.textContent = ok ? 'コピーしました' : '長押しでコピーしてください';
      setTimeout(function () { btn.textContent = old; }, 1800);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { done(true); }, function () { done(false); });
    } else {
      var ta = document.createElement('textarea');
      ta.value = text; document.body.appendChild(ta); ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (err) { ok = false; }
      document.body.removeChild(ta); done(ok);
    }
  });

  // 共有ボタン
  var box = document.querySelector('.share');
  if (box) {
    var surl = box.getAttribute('data-url'), stitle = box.getAttribute('data-title');
    var st = box.querySelector('.share-status');
    var say = function (m) { if (st) st.textContent = m; };
    var cp = box.querySelector('.share-copy');
    if (cp) cp.addEventListener('click', function () {
      var fallback = function () {
        var ta = document.createElement('textarea');
        ta.value = surl; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
        document.body.appendChild(ta); ta.select();
        var ok = false; try { ok = document.execCommand('copy'); } catch (err) {}
        document.body.removeChild(ta);
        say(ok ? 'リンクをコピーしました' : 'コピーできませんでした。アドレスバーから直接コピーしてください');
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(surl).then(function () { say('リンクをコピーしました'); }, fallback);
      } else { fallback(); }
    });
    var nat = box.querySelector('.share-native');
    if (nat && navigator.share) {
      nat.hidden = false;
      nat.querySelector('button').addEventListener('click', function () {
        navigator.share({ title: stitle, url: surl }).catch(function () {});
      });
    }
  }

  // 一覧の絞り込み
  var list = document.getElementById('tip-list');
  if (!list) return;
  var cards = Array.prototype.slice.call(list.querySelectorAll('.card'));
  var segBtns = Array.prototype.slice.call(document.querySelectorAll('.seg-btn'));
  var selPurpose = document.getElementById('f-purpose');
  var selFeature = document.getElementById('f-feature');
  var inpQ = document.getElementById('f-q');
  var count = document.getElementById('f-count');
  var empty = document.getElementById('f-empty');
  var level = '';
  var LIMIT = 12, expanded = false;
  var more = document.createElement('button');
  more.type = 'button'; more.className = 'more-btn'; more.hidden = true;
  list.parentNode.insertBefore(more, list.nextSibling);
  more.addEventListener('click', function () { expanded = true; apply(); });

  function apply() {
    var p = selPurpose.value, f = selFeature.value, q = inpQ.value.trim().toLowerCase();
    var n = 0, shown = 0;
    var plain = !level && !p && !f && !q;
    cards.forEach(function (c) {
      var ok = (!level || c.getAttribute('data-level') === level) &&
        (!p || c.getAttribute('data-purpose') === p) &&
        (!f || (' ' + c.getAttribute('data-features') + ' ').indexOf(' ' + f + ' ') >= 0) &&
        (!q || c.getAttribute('data-text').indexOf(q) >= 0);
      if (ok) n++;
      var show = ok && (!plain || expanded || shown < LIMIT);
      if (show) shown++;
      c.hidden = !show;
    });
    more.hidden = shown >= n;
    more.textContent = '残りの' + (n - shown) + '件も表示する';
    count.textContent = shown < n ? n + '件のうち、最初の' + shown + '件を表示中' : n + '件を表示中(全' + cards.length + '件)';
    empty.hidden = n !== 0;
    if (n === 0) { empty.textContent = hint(level, p, f, q); }
  }
  // 0件のとき、どの条件を外せば何件になるかを案内する
  function hint(lv, p, f, q) {
    function matches(l, pp, ff, qq) {
      var k = 0;
      cards.forEach(function (c) {
        if ((!l || c.getAttribute('data-level') === l) && (!pp || c.getAttribute('data-purpose') === pp) &&
          (!ff || (' ' + c.getAttribute('data-features') + ' ').indexOf(' ' + ff + ' ') >= 0) &&
          (!qq || c.getAttribute('data-text').indexOf(qq) >= 0)) k++;
      });
      return k;
    }
    var parts = [];
    if (lv) { var a = matches('', p, f, q); if (a) parts.push('難易度を「すべて」にすると' + a + '件'); }
    if (p) { var b = matches(lv, '', f, q); if (b) parts.push('目的を「すべて」にすると' + b + '件'); }
    if (f) { var d = matches(lv, p, '', q); if (d) parts.push('機能を「すべて」にすると' + d + '件'); }
    if (q) { var e = matches(lv, p, f, ''); if (e) parts.push('検索のことばを消すと' + e + '件'); }
    return '条件に合うものがありません。' + (parts.length ? parts.join('、') + '見つかります。' : '条件をゆるめてみてください。');
  }
  // 絞り込みを変えたとき、件数の表示が画面の外にあれば、そこまで移動する
  function reveal() {
    var r = count.getBoundingClientRect();
    if (r.top < 0 || r.top > window.innerHeight * 0.6) {
      var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      count.scrollIntoView({ behavior: calm ? 'auto' : 'smooth', block: 'start' });
    }
  }
  segBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      level = b.getAttribute('data-level');
      segBtns.forEach(function (x) { x.classList.toggle('is-on', x === b); x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      apply();
      reveal();
    });
    b.setAttribute('aria-pressed', b.classList.contains('is-on') ? 'true' : 'false');
  });
  [selPurpose, selFeature].forEach(function (s) { s.addEventListener('change', function () { apply(); reveal(); }); });
  inpQ.addEventListener('input', apply);
  apply();
})();
