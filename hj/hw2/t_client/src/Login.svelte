<script lang="ts">
    import { loginSuccessStore } from './stores'

    function login() {
        loginSuccessStore.set(true);
    }


</script>

<div>
    Test-login
    <button on:click="{login}">Mock Login Button</button>


</div>
