# Django-Strawberry-relay-pagination


```
query MyQuery {
  books {
    edges {
      node {
        title
        author
      }
      cursor
    }
    pageInfo {
      endCursor
      hasNextPage
    }
  }
}

```


```
query GetBooks {
  books(first: 5) {
    totalCount
    edges {
      node {
        id
        title
        author
      }
      cursor
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

To fetch next page, pass after using the returned endCursor
```
query NextBooks($after: String!) {
  books(first: 5, after: $after) {
    edges {
      node {
        id
        title
        author
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```