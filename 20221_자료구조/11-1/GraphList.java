class VertexNode {
  int data;
  VertexNode link;

  VertexNode( int data ) {
    this.data = data;
    this.link = null;
  }
}

class Queue {
  int Qsize;
  int front;
  int rear;
  int num;
  int[] queue;

  class EmptyQueueException extends RuntimeException {
    EmptyQueueException( ) { }
  }

  Queue( int capacity ) {
    this.num = this.front = this.rear = 0;
    this.Qsize = capacity;
    queue = new int[Qsize];
  }

  int add( int x ) {
    queue[rear++] = x;
    num += 1;
    if( rear == Qsize ) {
      rear = 0;
    }
    return x;
  }

  int remove() throws EmptyQueueException {
    if( num <= 0 ) {
      throw new EmptyQueueException( );
    }
    int x = queue[front++];
    num -= 1;
    if( front == Qsize ) {
      front = 0;
    }
    return x;
  }

  boolean isEmpty() {
    return num <= 0;
  }

  int size() {
    return num;
  }
}

interface GraphListVisitor {
  void visit( int data );
}

public class GraphList {
  boolean directed;
  int size;
  VertexNode[] heads;

  GraphList( int size, boolean directed ) {
    this.size = size;
    this.directed = directed;
    this.heads = new VertexNode[size];

    for( int i = 0; i < size; i++ ) {
      this.heads[i] = new VertexNode( i );
    }
  }

  void add( int v1, int v2 ) {
    VertexNode node = this.heads[v1];

    while( node.link != null ) {
      if( node.link.data == v2 ) {
        return;
      }
      node = node.link;
      if( !this.directed ) {
        this.add(v2, v1);
      }
    }
  }

  void bfs( int start, GraphListVisitor v ) {
    Queue q = new Queue( this.size );
    boolean visited[] = new boolean[this.size];
    for( int i = 0; i < this.size; i++ ) {
      visited[i] = false;
    }
    bfsInternal( start, v, q, visited );
  }

  void bfsInternal( int start, GraphListVisitor v, Queue q, boolean[] visited) {
    visited[start] = true;
    q.add( start );
    while( q.isEmpty() ) {
      int visit = q.remove();
      VertexNode select = this.heads[visit];
      int size = 1;

      while( select.link != null ) {
        size += 1;
      }

      while( size-- > 0 ) {
        int next = select.data;
        select = select.link;
        if( ! visited[next] ) {
          visited[next] = true;
          q.add( next );
        }
      }
    }
  }

  public static void main(String[] args) {
    GraphList G = new GraphList( 8, false );
    G.add( 0, 1 );
    G.add( 0, 2 );
    G.add( 1, 3 );
    G.add( 1, 4 );
    G.add( 2, 5 );
    G.add( 2, 6 );
    G.add( 3, 7 );
    G.add( 4, 7 );
    G.add( 5, 7 );
    G.add( 6, 7 );

    GraphListVisitor f = ( node ) -> {
      System.out.println( node + " -> " );
    };
    System.out.println("jhhh");

    G.bfs( 0, f );

    System.out.println();
    G.bfs( 3, f );
  }
}
