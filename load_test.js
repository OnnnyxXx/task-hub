import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
    vus: 10,
    duration: '10s',
};

export default function () {
    let res = http.get('https://ts1.pythonanywhere.com/');
    console.log('Response time was ' + String(res.timings.duration) + ' ms');

    check(res, {
        'X-Cache header exists': (r) => r.headers['X-Cache'] !== undefined,
        'Cache-Control header exists': (r) => r.headers['Cache-Control'] !== undefined,
        'Response status is 200': (r) => r.status === 200,
    });

    sleep(1);
}
