var app = new Vue({
    el: "#app",
    data: {
        res_data: ""
    },
    methods: {
        load_trekker: function () {
            window.location.href = '/' + 'trekker';
        },
        load_admin: function () {
            window.location.href = '/' + 'admin';
        },
        async fetch_call() {
            try {
                const response = await fetch("/api/trekker");
                const data = await response.json();
                this.res_data = JSON.stringify(data, null, 2);
            } catch (err) {
                console.log(err);
            }
        }
    },
    mounted() {
        this.fetch_call()
    }
})
