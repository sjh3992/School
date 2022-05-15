class VertexNode {
  int data;
  VertexNode link;

  VertexNode( int data ) {
    this.data = data;
    this.link = null;
  }
}

@functionalInterface
interface GraphListVisitor {
  void visit( int data );
}

class Queue {
  int Qsize;    // 큐의 용량
  int front;    // 첫 번째 요소 커서
  int rear;     // 마지막 요소 커서
  int num;      // 현재 데이터 수
  int[] queue;  // 큐 본체

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
    int x = que[front++];
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

public class GraphList {
  boolean directed; // 방향그래프 여부
  int size; // vertex의 개수
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

      for( int i = 0; i < select.size(); i++ ) {
        int next = select.remove();
        if( ! visited[next] ) {
          visited[next] = true;
          q.add( next );
        }
      }
    }
  }

  public static void main() {
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

    GraphListVisitor f = (node) -> {
      System.out.print( node.data + " -> " );
    };

    G.bfs( 0, f );
    System.out.println();
    G.bfs( 3, f );
  }
}
