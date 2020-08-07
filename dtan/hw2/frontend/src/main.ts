import App from './App.svelte';

const app = new App({
  target: document.body,
  //props: { },
  //target: document.getElementById("app"),
  props: { },
  hydrate: true,
});

export default app;