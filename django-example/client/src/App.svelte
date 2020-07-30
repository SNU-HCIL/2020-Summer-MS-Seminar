<script lang="ts">
import { onMount } from "svelte";
import axios from 'axios';

function getCookie(name: string): string {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		const cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

onMount(async () => {
	// "handshake" with server to set CSRF cookie
	await axios.get(
		'http://147.46.241.67:8055/todo/',
		{
			withCredentials: true
		}
	)
	// Now CSRF is set in browser cookie
	const csrftoken = getCookie('csrftoken');
	// You can make POST request now with the key
	const response = await axios.post(
		'http://147.46.241.67:8055/todo/tasks',
		{},
		{
			withCredentials: true,
			headers: {
				'X-CSRFToken': csrftoken
			}
		}
	)
	console.log({ response })
})
</script>

<main>
</main>
