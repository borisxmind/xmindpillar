/* effects.js – X mind Werbeagentur
   Progress Bar · Nav Shrink · Hamburger · Scroll Reveal · Counter · Testimonials · FAQ
   ──────────────────────────────────────────────────────────────────── */

/* 1. PROGRESS BAR */
(function(){
  var bar=document.getElementById('progress-bar');
  if(!bar)return;
  window.addEventListener('scroll',function(){
    var s=window.scrollY,t=document.documentElement.scrollHeight-window.innerHeight;
    bar.style.width=(t>0?s/t*100:0)+'%';
  },{passive:true});
})();

/* 2. NAV SHRINK */
(function(){
  var nav=document.getElementById('nav');
  if(!nav)return;
  window.addEventListener('scroll',function(){
    nav.classList.toggle('scrolled',window.scrollY>60);
  },{passive:true});
})();

/* 3. HAMBURGER */
(function(){
  var burger=document.getElementById('burger');
  var menu=document.getElementById('mobile-menu');
  if(!burger||!menu)return;
  function open(){menu.classList.add('open');burger.classList.add('open');burger.setAttribute('aria-expanded','true');document.body.style.overflow='hidden';}
  function close(){menu.classList.remove('open');burger.classList.remove('open');burger.setAttribute('aria-expanded','false');document.body.style.overflow='';}
  burger.addEventListener('click',function(){menu.classList.contains('open')?close():open();});
  menu.addEventListener('click',function(e){if(!e.target.closest('.mobile-drawer'))close();});
  menu.querySelectorAll('a').forEach(function(a){a.addEventListener('click',close);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
})();

/* 4. SCROLL REVEAL */
(function(){
  var els=document.querySelectorAll('[data-reveal]');
  var grps=document.querySelectorAll('[data-reveal-group]');
  if(!('IntersectionObserver' in window)){
    els.forEach(function(e){e.classList.add('revealed');});
    grps.forEach(function(e){e.classList.add('revealed');});
    return;
  }
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if(en.isIntersecting){en.target.classList.add('revealed');io.unobserve(en.target);}
    });
  },{threshold:0.1,rootMargin:'0px 0px -40px 0px'});
  els.forEach(function(e){io.observe(e);});
  grps.forEach(function(e){io.observe(e);});
})();

/* 5. STATS COUNTER */
(function(){
  var els=document.querySelectorAll('[data-count]');
  if(!els.length)return;
  function animate(el){
    var target=parseFloat(el.dataset.count);
    var suffix=el.dataset.suffix||'';
    var dur=1400,start=performance.now();
    (function tick(now){
      var p=Math.min((now-start)/dur,1),ease=1-Math.pow(1-p,4);
      el.textContent=Math.round(ease*target)+suffix;
      if(p<1)requestAnimationFrame(tick);
    })(start);
  }
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(en){if(en.isIntersecting){animate(en.target);io.unobserve(en.target);}});
  },{threshold:0.5});
  els.forEach(function(e){io.observe(e);});
})();

/* 6. TESTIMONIALS – Crossfade Grid */
(function(){
  var grid=document.getElementById('testi-grid');
  var dotsWrap=document.getElementById('slide-dots');
  if(!grid||!dotsWrap)return;
  var cards=grid.querySelectorAll('.testi-card');
  var pages=Math.ceil(cards.length/2);
  if(pages<2)return;
  var current=0,animating=false,autoTimer;
  for(var i=0;i<pages;i++){
    (function(idx){
      var d=document.createElement('button');
      d.className='dot'+(idx===0?' dot-active':'');
      d.setAttribute('aria-label','Seite '+(idx+1));
      d.addEventListener('click',function(){goTo(idx);resetAuto();});
      dotsWrap.appendChild(d);
    })(i);
  }
  function goTo(page){
    if(animating||page===current)return;
    animating=true;
    grid.classList.add('fading');
    setTimeout(function(){
      cards.forEach(function(c){
        parseInt(c.dataset.page)===page?c.removeAttribute('hidden'):c.setAttribute('hidden','');
      });
      current=page;
      dotsWrap.querySelectorAll('.dot').forEach(function(d,i){d.classList.toggle('dot-active',i===current);});
      grid.classList.remove('fading');
      animating=false;
    },380);
  }
  function startAuto(){autoTimer=setInterval(function(){goTo((current+1)%pages);},4500);}
  function resetAuto(){clearInterval(autoTimer);startAuto();}
  var pv=document.getElementById('slide-prev'),nx=document.getElementById('slide-next');
  if(pv)pv.addEventListener('click',function(){goTo((current-1+pages)%pages);resetAuto();});
  if(nx)nx.addEventListener('click',function(){goTo((current+1)%pages);resetAuto();});
  var tx=0;
  grid.addEventListener('touchstart',function(e){tx=e.touches[0].clientX;},{passive:true});
  grid.addEventListener('touchend',function(e){
    var dx=e.changedTouches[0].clientX-tx;
    if(Math.abs(dx)>40){goTo(dx<0?(current+1)%pages:(current-1+pages)%pages);resetAuto();}
  },{passive:true});
  startAuto();
})();

/* 7. FAQ ACCORDION */
(function(){
  document.querySelectorAll('.faq-btn').forEach(function(btn){
    btn.addEventListener('click',function(){
      var item=btn.closest('.faq-item');
      var isOpen=item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(function(o){o.classList.remove('open');});
      if(!isOpen)item.classList.add('open');
    });
  });
})();
