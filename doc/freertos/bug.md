## CVE-2021-31572

- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31572
- https://github.com/FreeRTOS/FreeRTOS-Kernel/pull/226/files

Add addition overflow check for stream buffer for the mostly theoretical case where you are allocating close to 4,294,967,296 bytes and the size_t rolls over.

Overflow happed when `size_t xBufferSizeBytes > 2^32 -  sizeof(StreamBuffer_t)`

```c
xBufferSizeBytes++;
pucAllocatedMemory = ( uint8_t * ) pvPortMalloc( xBufferSizeBytes + sizeof( StreamBuffer_t ) ); /*lint !e9079 malloc() only returns void*. */
```

```c
if( xBufferSizeBytes < ( xBufferSizeBytes + 1 + sizeof( StreamBuffer_t ) ) )
{
    xBufferSizeBytes++;
    pucAllocatedMemory = ( uint8_t * ) pvPortMalloc( xBufferSizeBytes + sizeof( StreamBuffer_t ) ); /*lint !e9079 malloc() only returns void*. */
}
else
{
    pucAllocatedMemory = NULL;
}
```

## Improve heap2 bounds checking

- https://github.com/FreeRTOS/FreeRTOS-Kernel/commit/c7a9a01c94987082b223d3e59969ede64363da63
- https://github.com/FreeRTOS/FreeRTOS-Kernel/pull/224

There was a mostly theoretical case where an overflow could occur if the size of the requested memory block is between 4,294,967,288 and 4,294,967,296 bytes.

```c
if( xWantedSize > 0 )
{
	xWantedSize += heapSTRUCT_SIZE;
// ...
```

```c
if( ( xWantedSize > 0 ) && 
   ( ( xWantedSize + heapSTRUCT_SIZE ) >  xWantedSize ) ) /* Overflow check */
{
    xWantedSize += heapSTRUCT_SIZE;

```

