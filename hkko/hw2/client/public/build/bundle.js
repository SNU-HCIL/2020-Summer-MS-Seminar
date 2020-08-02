var app=function(){"use strict";function t(){}const n=t=>t;function e(t){return t()}function o(){return Object.create(null)}function r(t){t.forEach(e)}function l(t){return"function"==typeof t}function u(t,n){return t!=t?n==n:t!==n||t&&"object"==typeof t||"function"==typeof t}const c="undefined"!=typeof window;let i=c?()=>window.performance.now():()=>Date.now(),s=c?t=>requestAnimationFrame(t):t;const f=new Set;function a(t){f.forEach(n=>{n.c(t)||(f.delete(n),n.f())}),0!==f.size&&s(a)}function d(t,n){t.appendChild(n)}function h(t,n,e){t.insertBefore(n,e||null)}function p(t){t.parentNode.removeChild(t)}function g(t,n){for(let e=0;e<t.length;e+=1)t[e]&&t[e].d(n)}function m(t){return document.createElement(t)}function $(t){return document.createTextNode(t)}function _(){return $(" ")}function y(t,n,e,o){return t.addEventListener(n,e,o),()=>t.removeEventListener(n,e,o)}function b(t,n,e){null==e?t.removeAttribute(n):t.getAttribute(n)!==e&&t.setAttribute(n,e)}function v(t,n){n=""+n,t.wholeText!==n&&(t.data=n)}const w=new Set;let x,E=0;function k(t,n,e,o,r,l,u,c=0){const i=16.666/o;let s="{\n";for(let t=0;t<=1;t+=i){const o=n+(e-n)*l(t);s+=100*t+`%{${u(o,1-o)}}\n`}const f=s+`100% {${u(e,1-e)}}\n}`,a=`__svelte_${function(t){let n=5381,e=t.length;for(;e--;)n=(n<<5)-n^t.charCodeAt(e);return n>>>0}(f)}_${c}`,d=t.ownerDocument;w.add(d);const h=d.__svelte_stylesheet||(d.__svelte_stylesheet=d.head.appendChild(m("style")).sheet),p=d.__svelte_rules||(d.__svelte_rules={});p[a]||(p[a]=!0,h.insertRule(`@keyframes ${a} ${f}`,h.cssRules.length));const g=t.style.animation||"";return t.style.animation=`${g?g+", ":""}${a} ${o}ms linear ${r}ms 1 both`,E+=1,a}function C(t,n){const e=(t.style.animation||"").split(", "),o=e.filter(n?t=>t.indexOf(n)<0:t=>-1===t.indexOf("__svelte")),r=e.length-o.length;r&&(t.style.animation=o.join(", "),E-=r,E||s(()=>{E||(w.forEach(t=>{const n=t.__svelte_stylesheet;let e=n.cssRules.length;for(;e--;)n.deleteRule(e);t.__svelte_rules={}}),w.clear())}))}function A(t){x=t}const O=[],X=[],j=[],N=[],R=Promise.resolve();let S=!1;function T(t){j.push(t)}let q=!1;const B=new Set;function L(){if(!q){q=!0;do{for(let t=0;t<O.length;t+=1){const n=O[t];A(n),P(n.$$)}for(O.length=0;X.length;)X.pop()();for(let t=0;t<j.length;t+=1){const n=j[t];B.has(n)||(B.add(n),n())}j.length=0}while(O.length);for(;N.length;)N.pop()();S=!1,q=!1,B.clear()}}function P(t){if(null!==t.fragment){t.update(),r(t.before_update);const n=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,n),t.after_update.forEach(T)}}let z;function D(t,n,e){t.dispatchEvent(function(t,n){const e=document.createEvent("CustomEvent");return e.initCustomEvent(t,!1,!1,n),e}(`${n?"intro":"outro"}${e}`))}const M=new Set;let F;function G(){F={r:0,c:[],p:F}}function I(){F.r||r(F.c),F=F.p}function H(t,n){t&&t.i&&(M.delete(t),t.i(n))}function J(t,n,e,o){if(t&&t.o){if(M.has(t))return;M.add(t),F.c.push(()=>{M.delete(t),o&&(e&&t.d(1),o())}),t.o(n)}}const K={duration:0};function Q(e,o,u,c){let d=o(e,u),h=c?0:1,p=null,g=null,m=null;function $(){m&&C(e,m)}function _(t,n){const e=t.b-h;return n*=Math.abs(e),{a:h,b:t.b,d:e,duration:n,start:t.start,end:t.start+n,group:t.group}}function y(o){const{delay:l=0,duration:u=300,easing:c=n,tick:y=t,css:b}=d||K,v={start:i()+l,b:o};o||(v.group=F,F.r+=1),p?g=v:(b&&($(),m=k(e,h,o,u,l,c,b)),o&&y(0,1),p=_(v,u),T(()=>D(e,o,"start")),function(t){let n;0===f.size&&s(a),new Promise(e=>{f.add(n={c:t,f:e})})}(t=>{if(g&&t>g.start&&(p=_(g,u),g=null,D(e,p.b,"start"),b&&($(),m=k(e,h,p.b,p.duration,0,c,d.css))),p)if(t>=p.end)y(h=p.b,1-h),D(e,p.b,"end"),g||(p.b?$():--p.group.r||r(p.group.c)),p=null;else if(t>=p.start){const n=t-p.start;h=p.a+p.d*c(n/p.duration),y(h,1-h)}return!(!p&&!g)}))}return{run(t){l(d)?(z||(z=Promise.resolve(),z.then(()=>{z=null})),z).then(()=>{d=d(),y(t)}):y(t)},end(){$(),p=g=null}}}function U(t,n){-1===t.$$.dirty[0]&&(O.push(t),S||(S=!0,R.then(L)),t.$$.dirty.fill(0)),t.$$.dirty[n/31|0]|=1<<n%31}function V(n,u,c,i,s,f,a=[-1]){const d=x;A(n);const h=u.props||{},g=n.$$={fragment:null,ctx:null,props:f,update:t,not_equal:s,bound:o(),on_mount:[],on_destroy:[],before_update:[],after_update:[],context:new Map(d?d.$$.context:[]),callbacks:o(),dirty:a};let m=!1;if(g.ctx=c?c(n,h,(t,e,...o)=>{const r=o.length?o[0]:e;return g.ctx&&s(g.ctx[t],g.ctx[t]=r)&&(g.bound[t]&&g.bound[t](r),m&&U(n,t)),e}):[],g.update(),m=!0,r(g.before_update),g.fragment=!!i&&i(g.ctx),u.target){if(u.hydrate){const t=function(t){return Array.from(t.childNodes)}(u.target);g.fragment&&g.fragment.l(t),t.forEach(p)}else g.fragment&&g.fragment.c();u.intro&&H(n.$$.fragment),function(t,n,o){const{fragment:u,on_mount:c,on_destroy:i,after_update:s}=t.$$;u&&u.m(n,o),T(()=>{const n=c.map(e).filter(l);i?i.push(...n):r(n),t.$$.on_mount=[]}),s.forEach(T)}(n,u.target,u.anchor),L()}A(d)}function W(t,{delay:e=0,duration:o=400,easing:r=n}){const l=+getComputedStyle(t).opacity;return{delay:e,duration:o,easing:r,css:t=>"opacity: "+t*l}}function Y(t,n,e){const o=t.slice();return o[15]=n[e],o[17]=e,o}function Z(t,n,e){const o=t.slice();return o[12]=n[e],o[14]=e,o}function tt(t){let n,e,o,r,l=t[15]+"";return{c(){n=m("div"),e=$(l)},m(t,o){h(t,n,o),d(n,e),r=!0},p(t,n){(!r||1&n)&&l!==(l=t[15]+"")&&v(e,l)},i(t){r||(T(()=>{o||(o=Q(n,W,{},!0)),o.run(1)}),r=!0)},o(t){o||(o=Q(n,W,{},!1)),o.run(0),r=!1},d(t){t&&p(n),t&&o&&o.end()}}}function nt(t){let n,e,o,r,l=t[2][t[14]][t[17]]&&tt(t);function u(...n){return t[8](t[14],t[17],...n)}return{c(){n=m("td"),l&&l.c(),b(n,"class","svelte-6j1saq")},m(t,c){h(t,n,c),l&&l.m(n,null),e=!0,o||(r=y(n,"click",u),o=!0)},p(e,o){(t=e)[2][t[14]][t[17]]?l?(l.p(t,o),4&o&&H(l,1)):(l=tt(t),l.c(),H(l,1),l.m(n,null)):l&&(G(),J(l,1,1,()=>{l=null}),I())},i(t){e||(H(l),e=!0)},o(t){J(l),e=!1},d(t){t&&p(n),l&&l.d(),o=!1,r()}}}function et(t){let n,e,o,r=t[12],l=[];for(let n=0;n<r.length;n+=1)l[n]=nt(Y(t,r,n));const u=t=>J(l[t],1,1,()=>{l[t]=null});return{c(){n=m("tr");for(let t=0;t<l.length;t+=1)l[t].c();e=_()},m(t,r){h(t,n,r);for(let t=0;t<l.length;t+=1)l[t].m(n,null);d(n,e),o=!0},p(t,o){if(21&o){let c;for(r=t[12],c=0;c<r.length;c+=1){const u=Y(t,r,c);l[c]?(l[c].p(u,o),H(l[c],1)):(l[c]=nt(u),l[c].c(),H(l[c],1),l[c].m(n,e))}for(G(),c=r.length;c<l.length;c+=1)u(c);I()}},i(t){if(!o){for(let t=0;t<r.length;t+=1)H(l[t]);o=!0}},o(t){l=l.filter(Boolean);for(let t=0;t<l.length;t+=1)J(l[t]);o=!1},d(t){t&&p(n),g(l,t)}}}function ot(n){let e,o,r,l;return{c(){e=m("h3"),o=$("Now: "),r=$(n[1]),l=$("'s turn...")},m(t,n){h(t,e,n),d(e,o),d(e,r),d(e,l)},p(t,n){2&n&&v(r,t[1])},i:t,o:t,d(t){t&&p(e)}}}function rt(t){let n,e,o,r,l;return{c(){n=m("div"),e=$(t[3]),o=$(" win!")},m(t,r){h(t,n,r),d(n,e),d(n,o),l=!0},p(t,n){(!l||8&n)&&v(e,t[3])},i(t){l||(T(()=>{r||(r=Q(n,ut,{duration:1e3},!0)),r.run(1)}),l=!0)},o(t){r||(r=Q(n,ut,{duration:1e3},!1)),r.run(0),l=!1},d(t){t&&p(n),t&&r&&r.end()}}}function lt(t){let n,e,o,l,u,c,i,s,f,a,$,v,w,x,E=t[0],k=[];for(let n=0;n<E.length;n+=1)k[n]=et(Z(t,E,n));const C=t=>J(k[t],1,1,()=>{k[t]=null}),A=[rt,ot],O=[];function X(t,n){return null!=t[3]?0:1}return s=X(t),f=O[s]=A[s](t),{c(){n=m("h2"),n.textContent="Let's play Tic Tac Toe!",e=_(),o=m("button"),o.textContent="Restart the game!",l=_(),u=m("table"),c=m("tbody");for(let t=0;t<k.length;t+=1)k[t].c();i=_(),f.c(),a=_(),$=m("button"),$.textContent="Go back to previous step!",b(u,"class","svelte-6j1saq")},m(r,f){h(r,n,f),h(r,e,f),h(r,o,f),h(r,l,f),h(r,u,f),d(u,c);for(let t=0;t<k.length;t+=1)k[t].m(c,null);h(r,i,f),O[s].m(r,f),h(r,a,f),h(r,$,f),v=!0,w||(x=[y(o,"click",t[7]),y($,"click",t[9])],w=!0)},p(t,[n]){if(21&n){let e;for(E=t[0],e=0;e<E.length;e+=1){const o=Z(t,E,e);k[e]?(k[e].p(o,n),H(k[e],1)):(k[e]=et(o),k[e].c(),H(k[e],1),k[e].m(c,null))}for(G(),e=E.length;e<k.length;e+=1)C(e);I()}let e=s;s=X(t),s===e?O[s].p(t,n):(G(),J(O[e],1,1,()=>{O[e]=null}),I(),f=O[s],f||(f=O[s]=A[s](t),f.c()),H(f,1),f.m(a.parentNode,a))},i(t){if(!v){for(let t=0;t<E.length;t+=1)H(k[t]);H(f),v=!0}},o(t){k=k.filter(Boolean);for(let t=0;t<k.length;t+=1)J(k[t]);J(f),v=!1},d(t){t&&p(n),t&&p(e),t&&p(o),t&&p(l),t&&p(u),g(k,t),t&&p(i),O[s].d(t),t&&p(a),t&&p($),w=!1,r(x)}}}function ut(t,n){return{duration:n.duration,css:t=>`background: rgb(0, 256, ${256*t});`+`transform: scale(${100*(t-.5)}) rotate(${120*t}deg);`}}function ct(t,n,e){let o=[["","",""],["","",""],["","",""]],r="X",l=[[!1,!1,!1],[!1,!1,!1],[!1,!1,!1]],u=null,c=[];function i(t,n){if(null===u&&!l[t][n]){e(0,o[t][n]=r,o);let i=[t,n,r];e(1,r="X"===r?"O":"X"),e(2,l[t][n]=!0,l),c.push(i);for(let t=0;t<f.length;t++){let n=["","",""];for(let e=0;e<3;e++){let r=parseInt(f[t][e]/3),l=f[t][e]%3;n[e]=o[r][l]}n[0]&&n[0]===n[1]&&n[0]===n[2]&&e(3,u=n[0])}}}function s(){e(3,u=null),e(0,o=[["","",""],["","",""],["","",""]]),e(1,r="X"),c=[],e(2,l=[[!1,!1,!1],[!1,!1,!1],[!1,!1,!1]])}const f=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];function a(){if(c.length>0&&null==u){let t=c.length;e(0,o[c[t-1][0]][c[t-1][1]]="",o),e(2,l[c[t-1][0]][c[t-1][1]]=!1,l),c.pop(),e(1,r="X"===r?"O":"X")}}return[o,r,l,u,i,s,a,()=>s(),(t,n)=>i(t,n),()=>a()]}return new class extends class{$destroy(){!function(t,n){const e=t.$$;null!==e.fragment&&(r(e.on_destroy),e.fragment&&e.fragment.d(n),e.on_destroy=e.fragment=null,e.ctx=[])}(this,1),this.$destroy=t}$on(t,n){const e=this.$$.callbacks[t]||(this.$$.callbacks[t]=[]);return e.push(n),()=>{const t=e.indexOf(n);-1!==t&&e.splice(t,1)}}$set(){}}{constructor(t){super(),V(this,t,ct,lt,u,{})}}({target:document.body,props:{name:"world"}})}();
//# sourceMappingURL=bundle.js.map