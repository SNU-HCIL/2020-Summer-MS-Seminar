<script lang="ts">
  import Board from "./Board.svelte";
  let username: string = "";
  //   let userpw: string = "";
  var loggedUser: string | null = null;
  let userHistory: Object | null = null;

  var json = new Object();

  function formSubmit() {
    console.log(username);
    json.type = "account";
    json.id = username;
    // json.password = userpw;

    var request = new XMLHttpRequest();
    request.open("POST", "http://0.0.0.0:8080/sign-in", true);
    request.setRequestHeader(
      "Content-Type",
      "application/x-www-form-urlencoded"
    );
    // request.responseType = 'json';
    console.log(JSON.stringify(json));
    request.send(JSON.stringify(json));

    request.onreadystatechange = () => {
      if (request.readyState == 4) {
        if (request.status == 200) {
          // isloggedIn = true;
		  console.log(request.responseText);
		  userHistory = JSON.parse(request.responseText);
		  loggedUser = username;
		  console.log(userHistory)
        } else {
          alert("error code: " + request.status);
        }
      }
    };
  }
</script>

<style>
  @import "https://fonts.googleapis.com/css?family=Quicksand";

  body {
    font-family: "Quicksand", sans-serif;
    font-weight: 500;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
  }

  .container {
    display: flex;
    -webkit-display: box;
    -moz-display: box;
    -ms-display: flexbox;
    -webkit-display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-content: center;
    padding: 6%;
    margin: 0;
  }

  form {
    background-color: #fff;
    padding: 2em;
    padding-bottom: 3em;
    border-radius: 8px;
    max-width: 400px;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 10px 40px -14px rgba(0, 0, 0, 0.25);
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
  }
  form input {
    color: #384047;
    background-color: #e8eeef;
    box-shadow: 0 1px 0 rgba(0, 0, 0, 0.03) inset;
    border: none;
    border-radius: 4px;
    padding: 1em;
    margin-bottom: 1.2em;
    width: 100%;
  }
  form input:focus {
    outline: none;
  }

  .button {
    font-weight: 600;
    text-align: center;
    font-size: 19px;
    color: #fff;
    background-color: #4bc970;
    width: 100%;
    border: none;
    border-radius: 4px;
    padding: 0.8em;
    margin-top: 1em;
    margin-bottom: 1em;
    cursor: pointer;
    overflow: hidden;
    transition: all 200ms ease-in-out;
    box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.3);
  }
  .button:hover {
    box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.3);
    transform: translateY(-4px);
  }
  @keyframes grow {
    to {
      transform: scale(2.5);
      opacity: 0;
    }
  }
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h2 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 3em;
    font-weight: 500;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>

<main>
  <!-- <form on:submit|preventDefault={formSubmit}>
		이름: <input bind:value={username} type='text'>
		비밀번호: <input bind:value={userpw} type='password'>
		<input type='submit' value='Log in'>
	</form> -->

  {#if !loggedUser}
    <div class="container">
      <form on:submit|preventDefault={formSubmit}>
        <h2>Tic-Tac-Toe</h2>
        <div class="form-content">
          <input
            bind:value={username}
            id="user-name"
            name="user-name"
            placeholder="user name"
            type="text" />
          <!-- <input
          bind:value={userpw}
          id="password"
          name="password"
          placeholder="password"
          type="password" /> -->
          <br />
          <input type="submit" class="button" value="Log in" />
        </div>
        <br />
      </form>
    </div>
  {:else}
    <Board username={username} winRate={userHistory}/>
  {/if}
</main>
