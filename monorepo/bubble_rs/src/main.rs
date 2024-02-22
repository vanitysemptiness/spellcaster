// main.rs
mod controllers;
mod bubble_model;
mod storage;

use warp::Filter;
#[tokio::main]
async fn main() {
    let get_hello = warp::path!("hello" / String)
        .map(controllers::hello_handler);

    let post_endpoint = warp::path!("post" / "endpoint")
        .and(warp::post())
        .and(warp::body::json())
        .map(controllers::post_handler);

    let routes = get_hello.or(post_endpoint);

    warp::serve(routes).run(([127, 0, 0, 1], 8080)).await;
}
