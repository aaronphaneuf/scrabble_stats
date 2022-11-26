<template>
    <div class="container">
        <div class="columns is-multiline">
            <img src="@/assets/players.png" width="150" height="83px">
            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Company</th>
                            <th>Contact Person</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="user in user"
                            v-bind:key="user.id">
                                <td><router-link :to="{ name: 'Users', params: { id: user.id}}">{{ user.name }}</router-link></td>
                                <td>{{ user.email }}</td>
                        </tr>
                    </tbody>
                </table>
                <router-link to="/dashboard/adduser" class="button is-dark">Add Player</router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default { 
        name: 'Players',
        data() { 
            return { 
                user: []
            }
        },
        mounted() { 
            this.getPlayers()
        },
        methods: { 
            async getPlayers() { 
                this.$store.commit('setIsLoading', true)

                axios
                    .get('/api/v1/user/')
                    .then(response => { 
                        this.user = response.data
                    })
                    .catch(error => { 
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>