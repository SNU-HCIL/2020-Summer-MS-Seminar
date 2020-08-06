<script lang="ts">
  import Game from './Game.svelte';
  import Signin from './Signin.svelte';
  import { writable } from 'svelte/store';
  import { onMount } from 'svelte';
  import axios from 'axios';
  import Cookies from 'js-cookie';
  import { Router, Link, Route } from 'svelte-routing';
  // https://www.npmjs.com/package/svelte-routing

  let promise = getLoginStatus();
  let id = '';
  let pw = '';

  function getCookie(name: string, documentCookie: string): string {
    let cookieValue = null;
    if (documentCookie && documentCookie !== '') {
      const cookies = documentCookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        console.log(cookie);
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }


  export function checkLoginStatus() {
    promise = getLoginStatus();
  }

  export const login = writable(false);

  async function getLoginStatus() {
    const res = await axios.get(
      'http://127.0.0.1:8000/',
      {
        withCredentials: true
      }
    );
    if (res.status === 200) {
      login.set(true);
      
      return;
    }
    else {
      login.set(false);
      throw new Error("");
    }
  }

  function signinClick() {
    axios.get(
      'http://127.0.0.1:8000/hello/',
      {
        withCredentials: true
      }
    ).then((response) => {
      console.log(response);
      const csrftoken = getCookie('csrftoken', response.headers["Cookie"]);
      console.log(csrftoken);
      const headers = {
        'X-CSRFToken': csrftoken
      };
      axios.post(
        'http://127.0.0.1:8000/auth/',
        {
          username: id,
          password: pw,
        },
        {
          withCredentials: true,
          headers
        }
      ).then(function (res) {
        checkLoginStatus();
      }).catch(function (err) {
        id = '';
        pw = '';
    })});
  }

</script>

<svelte:head>
  <title>dtan's Tic Tac Toe</title>
</svelte:head>

<main>
  {#await promise}
    <p>Connecting to server...</p>
  {:then}
    <Game />
  {:catch error}
    <Signin bind:userid={id} bind:pw={pw} click={signinClick} error={error}/>
  {/await}
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    font: 14px "Century Gothic", Futura, sans-serif;
    margin: 20px;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>